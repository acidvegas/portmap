# Portmap - Developed by acidvegas (https://github.com/acidvegas/portmap)
# portmap/_parser.py

import re


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

	entries = []

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
				proto_cells = cells
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
