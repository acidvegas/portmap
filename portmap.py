#!/usr/bin/env python3
# Portmap - Scrape TCP/UDP port assignments from Wikipedia into NDJSON - Developed by acidvegas (https://github.com/acidvegas/portmap)
# portmap.py

import argparse
import json
import logging
import os
import re
import sys
import urllib.parse
import urllib.request


WIKI_API        = 'https://en.wikipedia.org/w/api.php'
USER_AGENT      = 'portmap/1.0 (https://github.com/acidvegas/portmap)'
PAGE_TITLE      = 'List_of_TCP_and_UDP_port_numbers'
OUTPUT_FILE     = 'ports.ndjson'
HISTORY_FILE    = 'history.ndjson'
HISTORY_MD_FILE = 'history.md'
STATE_FILE      = '.last_revision'


def wiki_query(params: dict) -> dict:
	'''Make an authenticated request to the Wikipedia API.'''

	params['format'] = 'json'
	url = f'{WIKI_API}?{urllib.parse.urlencode(params)}'
	req = urllib.request.Request(url, headers={'User-Agent': USER_AGENT})

	with urllib.request.urlopen(req) as resp:
		return json.loads(resp.read())


def get_latest_revision() -> dict:
	'''Get the latest revision ID and timestamp from the Wikipedia API.'''

	data = wiki_query({
		'action'  : 'query',
		'titles'  : PAGE_TITLE,
		'prop'    : 'revisions',
		'rvprop'  : 'ids|timestamp',
		'rvlimit' : '1',
	})

	pages = data['query']['pages']
	page  = next(iter(pages.values()))
	rev   = page['revisions'][0]

	return {'revid': rev['revid'], 'timestamp': rev['timestamp']}


def needs_update(rev: dict) -> bool:
	'''Check if the local data is stale compared to the latest revision.'''

	if not os.path.exists(STATE_FILE) or not os.path.exists(OUTPUT_FILE):
		return True

	with open(STATE_FILE) as f:
		stored = json.load(f)

	return stored.get('revid') != rev['revid']


def save_state(rev: dict):
	'''Persist the latest revision info to disk.'''

	with open(STATE_FILE, 'w') as f:
		json.dump(rev, f)


def fetch_wikitext() -> str:
	'''Download the raw wikitext of the port list article.'''

	data = wiki_query({
		'action' : 'query',
		'titles' : PAGE_TITLE,
		'prop'   : 'revisions',
		'rvprop' : 'content',
		'rvslots': 'main',
	})

	pages = data['query']['pages']
	page  = next(iter(pages.values()))

	return page['revisions'][0]['slots']['main']['*']


def strip_markup(text: str) -> str:
	'''Remove wiki markup, leaving plain text.'''

	text = re.sub(r'<ref[^>]*>.*?</ref>',            '', text, flags=re.DOTALL)
	text = re.sub(r'<ref[^/]*/\s*>',                  '', text)
	text = re.sub(r'\[\[(?:[^\]|]*\|)?([^\]]*)\]\]', r'\1', text)
	text = re.sub(r"'''?",                             '', text)
	text = re.sub(r'<!--.*?-->',                       '', text, flags=re.DOTALL)

	return text.strip()


def parse_template(cell: str) -> str:
	'''Extract the status from a wiki template like {{Yes}}, {{N/A|Reserved}}, {{Maybe|Assigned}}.'''

	cell = cell.strip()

	m = re.search(r'\{\{([^}|]+)(?:\|([^}]*))?\}\}', cell)
	if not m:
		return ''

	name = m.group(1).strip().lower()
	arg  = (m.group(2) or '').strip().lower()

	if name == 'yes':
		return True
	elif name == 'no':
		return False
	elif name == 'unofficial':
		return 'unofficial'
	elif name == 'n/a':
		return arg if arg else 'n/a'
	elif name == 'maybe':
		return arg if arg else 'assigned'

	return name


def parse_port_range(raw: str) -> list:
	'''Turn a port cell like "5000-5500" or "80" into a list of ints.'''

	raw = raw.strip().replace(',', '')

	m = re.match(r'^(\d+)\s*[\u2013\u2014\u2212\-]+\s*(\d+)$', raw)
	if m:
		return list(range(int(m.group(1)), int(m.group(2)) + 1))

	m = re.match(r'^(\d+)$', raw)
	if m:
		return [int(m.group(1))]

	return []


def assign_protos(proto_cells: list) -> tuple:
	'''Parse protocol status cells, handling colspan spans.'''

	vals = ['', '', '', '']
	idx  = 0

	for cell in proto_cells:
		if idx >= 4:
			break

		colspan_m = re.match(r'colspan\s*=\s*(\d+)\s*(.*)', cell, re.DOTALL)
		if colspan_m:
			span  = int(colspan_m.group(1))
			value = parse_template(colspan_m.group(2))
			for _ in range(min(span, 4 - idx)):
				vals[idx] = value
				idx += 1
		else:
			vals[idx] = parse_template(cell)
			idx += 1

	return tuple(v if v != '' else False for v in vals)


def parse_tables(wikitext: str) -> list:
	'''Extract port entries from all sortable wikitables in the article.'''

	entries    = []
	last_port  = None
	rowspan_remaining = 0

	tables = re.findall(
		r'\{\|[^\n]*class="wikitable sortable.*?\|\}',
		wikitext,
		re.DOTALL
	)

	for table in tables:
		rows = re.split(r'^\|\-', table, flags=re.MULTILINE)
		last_port = None
		rowspan_remaining = 0

		for row in rows[1:]:
			lines = row.strip().split('\n')
			if not lines:
				continue

			combined = ''
			desc_lines = []

			for line in lines:
				stripped = line.strip()

				if not stripped or stripped.startswith('!'):
					continue

				cleaned = re.sub(r'<!--.*?-->', '', stripped).strip()

				if not cleaned:
					continue

				if combined and 'rowspan' in combined and '||' not in combined and '||' in cleaned:
					combined = combined + ' || ' + cleaned.lstrip('| ')
				elif cleaned.startswith('|') and '||' in cleaned and not combined:
					combined = cleaned
				elif cleaned.startswith('|') and '||' in cleaned and combined:
					combined = cleaned
				elif cleaned.startswith('|') and not combined:
					combined = cleaned
				elif combined and cleaned.startswith('|'):
					desc_lines.append(cleaned.lstrip('| '))
				elif combined:
					desc_lines.append(cleaned)

			if not combined:
				continue

			combined = combined.lstrip('| ')

			cells = [c.strip() for c in combined.split('||')]
			if not cells:
				continue

			# Extract port number from first cell
			first = cells[0]
			rowspan_m = re.search(r'rowspan\s*=\s*(\d+)', first)

			port_text = re.sub(r'rowspan\s*=\s*\d+\s*\|?\s*', '', first).strip()
			port_text = strip_markup(port_text)
			ports = parse_port_range(port_text)

			if ports:
				if rowspan_m:
					rowspan_remaining = int(rowspan_m.group(1)) - 1
				last_port = ports
				proto_cells = cells[1:]
			elif rowspan_remaining > 0:
				ports = last_port
				rowspan_remaining -= 1
				proto_cells = cells  # all cells are protocol cells (no port cell)
			else:
				continue

			if not ports:
				continue

			tcp, udp, sctp, dccp = assign_protos(proto_cells)

			desc = ' '.join(desc_lines)
			desc = strip_markup(desc)
			desc = re.sub(r'\{\{[^}]*\}\}', '', desc)
			desc = re.sub(r'\s+', ' ', desc).strip()

			for port in ports:
				entries.append({
					'port'        : port,
					'tcp'         : tcp,
					'udp'         : udp,
					'sctp'        : sctp,
					'dccp'        : dccp,
					'description' : desc,
				})

	return entries


def collapse_ranges(grouped: dict) -> list:
    '''Collapse consecutive ports with identical services into "x-y" ranges.'''

    records = []
    ports   = sorted(grouped)

    i = 0
    while i < len(ports):
        start = ports[i]
        svcs  = grouped[start]

        j = i + 1
        while j < len(ports) and ports[j] == start + (j - i) and grouped[ports[j]] == svcs:
            j += 1

        end = ports[j - 1]
        port_key = f'{start}-{end}' if end > start else start
        records.append({'port': port_key, 'services': svcs})
        i = j

    return records


def status_label(val) -> str:
    '''Format a protocol status for the markdown table.'''

    if val is True:
        return 'Yes'
    elif val is False:
        return ''
    else:
        return val.capitalize()


def format_ports_markdown(records: list) -> str:
    '''Render port records as a markdown table.'''

    lines = [
        '# TCP/UDP Port Numbers\n',
        '| Port | TCP | UDP | SCTP | DCCP | Description |',
        '|-----:|:---:|:---:|:----:|:----:|:------------|',
    ]

    for rec in records:
        port = rec['port']
        for svc in rec['services']:
            tcp  = status_label(svc['tcp'])
            udp  = status_label(svc['udp'])
            sctp = status_label(svc['sctp'])
            dccp = status_label(svc['dccp'])
            desc = svc['description']
            lines.append(f'| {port} | {tcp} | {udp} | {sctp} | {dccp} | {desc} |')

    return '\n'.join(lines) + '\n'


def format_history_markdown() -> str:
    '''Render revision history as a markdown table.'''

    if not os.path.exists(HISTORY_FILE):
        return ''

    with open(HISTORY_FILE) as f:
        revisions = [json.loads(line) for line in f if line.strip()]

    if not revisions:
        return ''

    lines = [
        '# Revision History\n',
        '| Date | User | Size | Comment |',
        '|:-----|:-----|-----:|:--------|',
    ]

    for rev in revisions:
        date    = rev['timestamp'].replace('T', ' ').rstrip('Z')
        user    = rev.get('user', '')
        size    = f'{rev.get("size", 0):,}'
        comment = rev.get('comment', '').replace('|', '\\|')
        lines.append(f'| {date} | {user} | {size} | {comment} |')

    return '\n'.join(lines) + '\n'


def write_markdown(records: list, path: str):
    '''Write port records as a markdown file.'''

    with open(path, 'w') as f:
        f.write(format_ports_markdown(records))


def write_history_markdown():
    '''Write revision history as a markdown file.'''

    md = format_history_markdown()
    if md:
        with open(HISTORY_MD_FILE, 'w') as f:
            f.write(md)


def fetch_and_save() -> list:
    '''Scrape Wikipedia, write NDJSON + markdown + history, return records.'''

    rev = get_latest_revision()

    logging.info(f'Fetching rev {rev["revid"]} ({rev["timestamp"]})...')

    wikitext = fetch_wikitext()
    entries  = parse_tables(wikitext)

    grouped = {}
    for entry in entries:
        port = entry.pop('port')
        grouped.setdefault(port, []).append(entry)

    records = collapse_ranges(grouped)

    with open(OUTPUT_FILE, 'w') as f:
        for rec in records:
            f.write(json.dumps(rec, ensure_ascii=False) + '\n')

    write_markdown(records, 'ports.md')

    logging.debug('Fetching revision history...')
    revisions = fetch_history()
    with open(HISTORY_FILE, 'w') as f:
        for entry in revisions:
            f.write(json.dumps(entry, ensure_ascii=False) + '\n')
    logging.debug(f'Saved {len(revisions):,} revisions to {HISTORY_FILE}')

    write_history_markdown()

    save_state(rev)

    return records


def load_records() -> list:
    '''Load records from the local NDJSON file.'''

    with open(OUTPUT_FILE) as f:
        return [json.loads(line) for line in f]


def ensure_data() -> list:
    '''Return current records, fetching from Wikipedia only if stale.'''

    try:
        rev = get_latest_revision()
    except Exception:
        if os.path.exists(OUTPUT_FILE):
            logging.warning('Offline — using cached data')
            return load_records()
        raise

    if needs_update(rev):
        return fetch_and_save()

    logging.info(f'Up to date (rev {rev["revid"]})')
    return load_records()


def port_in_record(rec, port: int) -> bool:
    '''Check if a single port number falls within a record's port/range.'''

    p = rec['port']

    if isinstance(p, int):
        return p == port

    if isinstance(p, str) and '-' in p:
        lo, hi = p.split('-', 1)
        return int(lo) <= port <= int(hi)

    return False


def filter_records(records: list, ports: list) -> list:
    '''Return only records matching any of the requested port numbers.'''

    return [rec for rec in records if any(port_in_record(rec, p) for p in ports)]


def search_records(records: list, term: str) -> list:
    '''Return records where any service description contains the search term.'''

    term = term.lower()
    results = []

    for rec in records:
        matching = [svc for svc in rec['services'] if term in svc['description'].lower()]
        if matching:
            results.append({**rec, 'services': matching})

    return results


C_RESET = '\033[0m'
C_BOLD  = '\033[1m'
C_CYAN  = '\033[36m'
C_GREEN = '\033[32m'
C_RED   = '\033[31m'
C_YELL  = '\033[33m'
C_WHITE = '\033[37m'
C_DIM   = '\033[2m'


def color_status(val) -> str:
    '''Colorize a protocol status value.'''

    if val is True:
        return f'{C_GREEN}Yes{C_RESET}'
    elif val is False:
        return f'{C_DIM}--{C_RESET}'
    elif val in ('unofficial',):
        return f'{C_YELL}Unofficial{C_RESET}'
    elif val in ('assigned',):
        return f'{C_YELL}Assigned{C_RESET}'
    elif val in ('reserved',):
        return f'{C_RED}Reserved{C_RESET}'
    else:
        return f'{C_YELL}{str(val).capitalize()}{C_RESET}'


def visible_len(s: str) -> int:
    '''Length of string ignoring ANSI escape codes.'''

    return len(re.sub(r'\033\[[0-9;]*m', '', s))


def rpad(s: str, width: int) -> str:
    '''Right-pad a string accounting for ANSI codes.'''

    return s + ' ' * max(0, width - visible_len(s))


def print_table(records: list):
    '''Print records as a colored, aligned table.'''

    W_PORT = 12
    W_PROTO = 12
    W_DESC = 80

    hdr = (
        f'{C_BOLD}{C_WHITE}'
        f'{"PORT".ljust(W_PORT)}'
        f'{"TCP".ljust(W_PROTO)}'
        f'{"UDP".ljust(W_PROTO)}'
        f'{"SCTP".ljust(W_PROTO)}'
        f'{"DCCP".ljust(W_PROTO)}'
        f'{"DESCRIPTION"}'
        f'{C_RESET}'
    )
    sep = f'{C_DIM}{"─" * W_PORT}{"─" * W_PROTO}{"─" * W_PROTO}{"─" * W_PROTO}{"─" * W_PROTO}{"─" * W_DESC}{C_RESET}'

    print(hdr)
    print(sep)

    for rec in records:
        port_str = str(rec['port'])

        for i, svc in enumerate(rec['services']):
            port_col = f'{C_CYAN}{C_BOLD}{port_str.ljust(W_PORT)}{C_RESET}' if i == 0 else ' ' * W_PORT
            tcp_col  = rpad(color_status(svc['tcp']),  W_PROTO)
            udp_col  = rpad(color_status(svc['udp']),  W_PROTO)
            sctp_col = rpad(color_status(svc['sctp']), W_PROTO)
            dccp_col = rpad(color_status(svc['dccp']), W_PROTO)
            desc     = svc['description']

            print(f'{port_col}{tcp_col}{udp_col}{sctp_col}{dccp_col}{desc}')


def fetch_history(days: int = 365) -> list:
    '''Fetch the revision history for the past N days from the Wikipedia API.'''

    from datetime import datetime, timedelta, timezone

    cutoff  = (datetime.now(timezone.utc) - timedelta(days=days)).strftime('%Y-%m-%dT%H:%M:%SZ')
    revisions = []
    rvcontinue = None

    while True:
        params = {
            'action'  : 'query',
            'titles'  : PAGE_TITLE,
            'prop'    : 'revisions',
            'rvprop'  : 'ids|timestamp|user|size|comment',
            'rvlimit' : 'max',
            'rvstart' : datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
            'rvend'   : cutoff,
            'rvdir'   : 'older',
        }

        if rvcontinue:
            params['rvcontinue'] = rvcontinue

        data  = wiki_query(params)
        pages = data['query']['pages']
        page  = next(iter(pages.values()))

        revisions.extend(page.get('revisions', []))

        if 'continue' in data:
            rvcontinue = data['continue']['rvcontinue']
        else:
            break

    return revisions


def main():
    parser = argparse.ArgumentParser(description='TCP/UDP port number lookup from Wikipedia')
    parser.add_argument('ports',  nargs='?', help='Comma-separated port numbers to look up')
    parser.add_argument('-d',     action='store_true', help='Enable debug logging')
    parser.add_argument('-j',     action='store_true', help='Output as NDJSON')
    parser.add_argument('-md',    action='store_true', help='Output as Markdown (ports + history)')
    parser.add_argument('-s',     metavar='TERM', help='Search descriptions for a keyword')
    parser.add_argument('-u',     action='store_true', help='Force update from Wikipedia')
    parser.add_argument('--history', type=int, metavar='DAYS', nargs='?', const=365,
                        help='Fetch history only (default: 365 days)')
    args = parser.parse_args()

    if args.j or args.md:
        logging.basicConfig(level=logging.CRITICAL)
    else:
        logging.basicConfig(
            level  = logging.DEBUG if args.d else logging.INFO,
            format = '%(levelname)s %(message)s',
        )

    if args.history is not None:
        logging.info(f'Fetching {args.history} days of revision history...')
        revisions = fetch_history(args.history)
        with open(HISTORY_FILE, 'w') as f:
            for rev in revisions:
                f.write(json.dumps(rev, ensure_ascii=False) + '\n')
        write_history_markdown()
        logging.info(f'Wrote {len(revisions)} revisions to {HISTORY_FILE} and {HISTORY_MD_FILE}')
        return

    if args.u:
        records = fetch_and_save()
    else:
        records = ensure_data()

    if args.ports:
        try:
            wanted = [int(p.strip()) for p in args.ports.split(',')]
        except ValueError:
            logging.error('Ports must be comma-separated integers')
            sys.exit(1)
        records = filter_records(records, wanted)

    if args.s:
        records = search_records(records, args.s)

    if not records:
        logging.error('No matching records found.')
        sys.exit(1)

    if args.j:
        for rec in records:
            print(json.dumps(rec, ensure_ascii=False))
    elif args.md:
        print(format_ports_markdown(records))
        history_md = format_history_markdown()
        if history_md:
            print(history_md)
    else:
        print_table(records)



if __name__ == '__main__':
    main()