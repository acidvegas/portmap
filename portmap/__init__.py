# Portmap - Developed by acidvegas (https://github.com/acidvegas/portmap)
# portmap/__init__.py

'''Scrape the Wikipedia list of TCP/UDP port numbers into a local database with revision tracking.'''

__version__ = '2.0.0'
__all__     = ['PortMap', '__version__']

import json
import logging
from pathlib import Path

from ._wiki   import get_latest_revision, fetch_wikitext, fetch_history
from ._parser import parse_tables, collapse_ranges
from ._format import format_ports_markdown, format_history_markdown


class PortMap:
	'''TCP/UDP port number database backed by Wikipedia.

	:param data_dir: Directory for storing NDJSON, markdown, and state files.
	'''

	PORTS_NDJSON   = 'ports.ndjson'
	HISTORY_NDJSON = 'history.ndjson'
	PORTS_MD       = 'ports.md'
	HISTORY_MD     = 'history.md'
	STATE_FILE     = '.last_revision'

	def __init__(self, data_dir: str = '.'):
		self._dir = Path(data_dir).expanduser().resolve()
		self._dir.mkdir(parents=True, exist_ok=True)


	def _path(self, name: str) -> Path:
		return self._dir / name


	def _needs_update(self, rev: dict) -> bool:
		state = self._path(self.STATE_FILE)
		ports = self._path(self.PORTS_NDJSON)

		if not state.exists() or not ports.exists():
			return True

		with open(state) as f:
			stored = json.load(f)

		return stored.get('revid') != rev['revid']


	def _save_state(self, rev: dict):
		with open(self._path(self.STATE_FILE), 'w') as f:
			json.dump(rev, f)


	def _write_ndjson(self, name: str, items: list):
		with open(self._path(name), 'w') as f:
			for item in items:
				f.write(json.dumps(item, ensure_ascii=False) + '\n')


	def _write_file(self, name: str, content: str):
		if content:
			with open(self._path(name), 'w') as f:
				f.write(content)


	def update(self, force: bool = False) -> list:
		'''Fetch latest port data from Wikipedia.

		Only hits the network when the article has actually changed,
		unless *force* is True. Writes NDJSON + markdown files to *data_dir*.

		:param force: Re-download even if local data is current.
		:return:      List of port record dicts.
		'''

		rev = get_latest_revision()

		if not force and not self._needs_update(rev):
			logging.info(f'Up to date (rev {rev["revid"]})')
			return self.load()

		logging.info(f'Fetching rev {rev["revid"]} ({rev["timestamp"]})...')

		wikitext = fetch_wikitext()
		entries  = parse_tables(wikitext)

		grouped = {}
		for entry in entries:
			port = entry.pop('port')
			grouped.setdefault(port, []).append(entry)

		records = collapse_ranges(grouped)

		self._write_ndjson(self.PORTS_NDJSON, records)
		self._write_file(self.PORTS_MD, format_ports_markdown(records))

		logging.debug('Fetching revision history...')
		revisions = fetch_history()
		self._write_ndjson(self.HISTORY_NDJSON, revisions)
		self._write_file(self.HISTORY_MD, format_history_markdown(revisions))

		self._save_state(rev)

		return records


	def load(self) -> list:
		'''Load cached port records from disk.

		:return: List of port record dicts, or [] if no cache exists.
		'''

		path = self._path(self.PORTS_NDJSON)
		if not path.exists():
			return []

		with open(path) as f:
			return [json.loads(line) for line in f if line.strip()]


	def load_history(self) -> list:
		'''Load cached revision history from disk.

		:return: List of revision dicts, or [] if no cache exists.
		'''

		path = self._path(self.HISTORY_NDJSON)
		if not path.exists():
			return []

		with open(path) as f:
			return [json.loads(line) for line in f if line.strip()]


	def lookup(self, *ports: int) -> list:
		'''Look up specific port numbers.

		Auto-fetches from Wikipedia if no local data exists.

		:param ports: One or more port numbers (ints).
		:return:      Matching port record dicts.
		'''

		records = self._ensure_data()
		return _filter_records(records, list(ports))


	def search(self, term: str) -> list:
		'''Search port descriptions for a keyword.

		Auto-fetches from Wikipedia if no local data exists.

		:param term: Case-insensitive search string.
		:return:     Matching port record dicts.
		'''

		records = self._ensure_data()
		return _search_records(records, term)


	def history(self, days: int = 365) -> list:
		'''Fetch revision history for the past N days from Wikipedia.

		:param days: Number of days of history to retrieve.
		:return:     List of revision dicts.
		'''

		revisions = fetch_history(days)
		self._write_ndjson(self.HISTORY_NDJSON, revisions)
		self._write_file(self.HISTORY_MD, format_history_markdown(revisions))
		return revisions


	def _ensure_data(self) -> list:
		'''Return records, fetching only if stale or missing.'''

		try:
			rev = get_latest_revision()
		except Exception:
			records = self.load()
			if records:
				logging.warning('Offline — using cached data')
				return records
			raise

		if self._needs_update(rev):
			return self.update(force=True)

		return self.load()


def _port_in_record(rec: dict, port: int) -> bool:
	'''Check if a single port number falls within a record's port/range.'''

	p = rec['port']

	if isinstance(p, int):
		return p == port

	if isinstance(p, str) and '-' in p:
		lo, hi = p.split('-', 1)
		return int(lo) <= port <= int(hi)

	return False


def _filter_records(records: list, ports: list) -> list:
	'''Return only records matching any of the requested port numbers.'''

	return [rec for rec in records if any(_port_in_record(rec, p) for p in ports)]


def _search_records(records: list, term: str) -> list:
	'''Return records where any service description contains the search term.'''

	term = term.lower()
	results = []

	for rec in records:
		matching = [svc for svc in rec['services'] if term in svc['description'].lower()]
		if matching:
			results.append({**rec, 'services': matching})

	return results
