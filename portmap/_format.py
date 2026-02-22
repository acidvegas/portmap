# Portmap - Developed by acidvegas (https://github.com/acidvegas/portmap)
# portmap/_format.py

import re


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


def format_history_markdown(revisions: list) -> str:
	'''Render revision history as a markdown table.'''

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


C_RESET = '\033[0m'
C_BOLD  = '\033[1m'
C_CYAN  = '\033[36m'
C_GREEN = '\033[32m'
C_RED   = '\033[31m'
C_YELL  = '\033[33m'
C_WHITE = '\033[37m'
C_DIM   = '\033[2m'


def color_status(val) -> str:
	'''Colorize a protocol status value for terminal output.'''

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
	'''Print records as a colored, aligned table to stdout.'''

	W_PORT  = 12
	W_PROTO = 12
	W_DESC  = 80

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
