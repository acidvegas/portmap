# Portmap - Developed by acidvegas (https://github.com/acidvegas/portmap)
# portmap/__main__.py

'''CLI entry point for portmap — run with `python -m portmap` or the `portmap` console script.'''

import argparse
import json
import logging
import sys

from . import PortMap, _filter_records, _search_records
from ._format import format_ports_markdown, format_history_markdown, print_table


def main():
	parser = argparse.ArgumentParser(
		prog        = 'portmap',
		description = 'TCP/UDP port number lookup from Wikipedia',
	)
	parser.add_argument('ports',       nargs='?', help='Comma-separated port numbers to look up')
	parser.add_argument('-d',          action='store_true', help='Enable debug logging')
	parser.add_argument('-j',          action='store_true', help='Output as NDJSON')
	parser.add_argument('-md',         action='store_true', help='Output as Markdown (ports + history)')
	parser.add_argument('-s',          metavar='TERM', help='Search descriptions for a keyword')
	parser.add_argument('-u',          action='store_true', help='Force update from Wikipedia')
	parser.add_argument('--data-dir',  default='.', metavar='DIR', help='Directory for data files (default: current dir)')
	parser.add_argument('--history',   type=int, metavar='DAYS', nargs='?', const=365,
	                    help='Fetch history only (default: 365 days)')
	parser.add_argument('--serve',     action='store_true', help='Start the JSON API server')
	parser.add_argument('--host',      default='127.0.0.1', metavar='ADDR', help='API server bind address (default: 127.0.0.1)')
	parser.add_argument('--port',      type=int, default=6660, metavar='PORT', help='API server bind port (default: 6660)')
	args = parser.parse_args()

	if args.j or args.md:
		logging.basicConfig(level=logging.CRITICAL)
	else:
		logging.basicConfig(
			level  = logging.DEBUG if args.d else logging.INFO,
			format = '%(levelname)s %(message)s',
		)

	pm = PortMap(data_dir=args.data_dir)

	if args.serve:
		if not pm.load():
			logging.info('No cached data — fetching from Wikipedia first...')
			pm.update(force=True)
		from ._server import serve
		serve(pm, host=args.host, port=args.port)
		return

	if args.history is not None:
		logging.info(f'Fetching {args.history} days of revision history...')
		revisions = pm.history(args.history)
		logging.info(f'Wrote {len(revisions)} revisions to {pm._dir}')
		return

	if args.u:
		records = pm.update(force=True)
	else:
		records = pm.update()

	if args.ports:
		try:
			wanted = [int(p.strip()) for p in args.ports.split(',')]
		except ValueError:
			logging.error('Ports must be comma-separated integers')
			sys.exit(1)
		records = _filter_records(records, wanted)

	if args.s:
		records = _search_records(records, args.s)

	if not records:
		logging.error('No matching records found.')
		sys.exit(1)

	if args.j:
		for rec in records:
			print(json.dumps(rec, ensure_ascii=False))
	elif args.md:
		print(format_ports_markdown(records))
		revisions = pm.load_history()
		if revisions:
			print(format_history_markdown(revisions))
	else:
		print_table(records)


if __name__ == '__main__':
	main()
