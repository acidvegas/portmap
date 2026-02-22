# Portmap - Developed by acidvegas (https://github.com/acidvegas/portmap)
# portmap/_wiki.py

import json
import urllib.parse
import urllib.request

WIKI_API   = 'https://en.wikipedia.org/w/api.php'
USER_AGENT = 'portmap/2.0 (https://github.com/acidvegas/portmap)'
PAGE_TITLE = 'List_of_TCP_and_UDP_port_numbers'


def wiki_query(params: dict) -> dict:
	'''Make a request to the Wikipedia API.'''

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


def fetch_history(days: int = 365) -> list:
	'''Fetch the revision history for the past N days from the Wikipedia API.'''

	from datetime import datetime, timedelta, timezone

	cutoff     = (datetime.now(timezone.utc) - timedelta(days=days)).strftime('%Y-%m-%dT%H:%M:%SZ')
	revisions  = []
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
