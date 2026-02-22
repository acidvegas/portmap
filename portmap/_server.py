# Portmap - Developed by acidvegas (https://github.com/acidvegas/portmap)
# portmap/_server.py

'''Minimal JSON API server for portmap — stdlib only, no frameworks.'''

import json
import logging
import re
import urllib.parse
from http.server import HTTPServer, BaseHTTPRequestHandler

from . import PortMap, __version__, _filter_records, _search_records

MAX_SEARCH_LEN = 20
MAX_LIMIT      = 100
MAX_PORTS      = 10
SEARCH_RE      = re.compile(r'^[\w\s\-\.\/\(\)\+\#\&\,\:]+$', re.UNICODE)


class _Handler(BaseHTTPRequestHandler):
	'''Request handler that routes GET requests to portmap data.'''

	pm: PortMap = None

	server_version = f'portmap/{__version__}'

	def log_message(self, fmt, *args):
		logging.info(f'{self.address_string()} {fmt % args}')

	# ------------------------------------------------------------------

	def do_GET(self):
		self._route()

	def do_HEAD(self):
		self._route(head=True)

	def do_POST(self):
		self._error(405, 'Method not allowed')

	do_PUT = do_DELETE = do_PATCH = do_POST

	# ------------------------------------------------------------------

	def _route(self, head: bool = False):
		parsed = urllib.parse.urlparse(self.path)
		path   = parsed.path.rstrip('/')
		params = urllib.parse.parse_qs(parsed.query)

		try:
			if path in ('', '/'):
				body = self._index()
			elif path == '/ports':
				body = self._list_ports(params)
			elif path.startswith('/ports/'):
				body = self._lookup(path[7:])
			elif path == '/history':
				body = self._get_history(params)
			else:
				return self._error(404, 'Not found')
		except _APIError as exc:
			return self._error(exc.code, str(exc))
		except Exception:
			logging.exception('Internal error')
			return self._error(500, 'Internal server error')

		payload = json.dumps(body, ensure_ascii=False).encode()
		self.send_response(200)
		self._headers(len(payload))
		if not head:
			self.wfile.write(payload)

	# ------------------------------------------------------------------

	def _index(self) -> dict:
		return {
			'name'      : 'portmap',
			'version'   : __version__,
			'endpoints' : {
				'GET /ports'              : 'List all ports. Query: ?search=TERM&limit=N&offset=N',
				'GET /ports/<number>'     : 'Lookup port(s). Comma-separated, e.g. /ports/80,443',
				'GET /history'            : 'Revision history. Query: ?limit=N&offset=N',
			},
		}


	def _list_ports(self, params: dict) -> dict:
		records = self.pm.load()

		search = self._param_str(params, 'search')
		if search:
			records = _search_records(records, search)

		total   = len(records)
		limit   = self._param_int(params, 'limit',  total, 1, MAX_LIMIT)
		offset  = self._param_int(params, 'offset', 0,     0, max(total - 1, 0))
		records = records[offset:offset + limit]

		return {'total': total, 'limit': limit, 'offset': offset, 'results': records}


	def _lookup(self, raw: str) -> dict:
		raw = raw.strip()

		if not raw:
			raise _APIError(400, 'Port number required')

		if not re.match(r'^[\d,]+$', raw):
			raise _APIError(400, 'Port numbers must be integers separated by commas')

		parts = [p.strip() for p in raw.split(',') if p.strip()]

		if len(parts) > MAX_PORTS:
			raise _APIError(400, f'Too many ports (max {MAX_PORTS})')

		ports = []
		for p in parts:
			try:
				n = int(p)
			except ValueError:
				raise _APIError(400, f'Invalid port number: {p}')
			if n < 0 or n > 65535:
				raise _APIError(400, f'Port out of range (0-65535): {n}')
			ports.append(n)

		records = self.pm.load()
		results = _filter_records(records, ports)

		return {'ports': ports, 'results': results}


	def _get_history(self, params: dict) -> dict:
		revisions = self.pm.load_history()
		total     = len(revisions)
		limit     = self._param_int(params, 'limit',  total, 1, MAX_LIMIT)
		offset    = self._param_int(params, 'offset', 0,     0, max(total - 1, 0))
		revisions = revisions[offset:offset + limit]

		return {'total': total, 'limit': limit, 'offset': offset, 'results': revisions}

	# ------------------------------------------------------------------

	@staticmethod
	def _param_int(params: dict, key: str, default: int, lo: int, hi: int) -> int:
		vals = params.get(key)
		if not vals:
			return default
		raw = vals[0]
		if not raw.isdigit():
			raise _APIError(400, f'"{key}" must be a positive integer')
		n = int(raw)
		if n < lo or n > hi:
			raise _APIError(400, f'"{key}" out of range ({lo}-{hi})')
		return n


	@staticmethod
	def _param_str(params: dict, key: str) -> str:
		vals = params.get(key)
		if not vals:
			return ''
		raw = vals[0].strip()
		if len(raw) > MAX_SEARCH_LEN:
			raise _APIError(400, f'"{key}" too long (max {MAX_SEARCH_LEN} chars)')
		if raw and not SEARCH_RE.match(raw):
			raise _APIError(400, f'"{key}" contains invalid characters')
		return raw


	def _headers(self, length: int):
		self.send_header('Content-Type',            'application/json; charset=utf-8')
		self.send_header('Content-Length',           str(length))
		self.send_header('X-Content-Type-Options',   'nosniff')
		self.send_header('Cache-Control',            'no-store')
		self.end_headers()


	def _error(self, code: int, message: str):
		body = json.dumps({'error': message}, ensure_ascii=False).encode()
		self.send_response(code)
		self._headers(len(body))
		self.wfile.write(body)


class _APIError(Exception):
	def __init__(self, code: int, message: str):
		super().__init__(message)
		self.code = code


def serve(pm: PortMap, host: str = '127.0.0.1', port: int = 6660):
	'''Start the portmap API server.

	:param pm:   PortMap instance to serve data from.
	:param host: Bind address (default: 127.0.0.1).
	:param port: Bind port (default: 6660).
	'''

	_Handler.pm = pm

	httpd = HTTPServer((host, port), _Handler)
	logging.info(f'Serving portmap API on http://{host}:{port}')

	try:
		httpd.serve_forever()
	except KeyboardInterrupt:
		pass
	finally:
		httpd.server_close()
		logging.info('Server stopped')
