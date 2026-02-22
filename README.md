# portmap

Scrape the [Wikipedia list of TCP/UDP port numbers](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers) into a local NDJSON database with revision tracking. Only fetches from Wikipedia when the article has actually changed.

## Install

```bash
pip install portmapper
```

## Python Library

```python
from portmap import PortMap

pm = PortMap(data_dir='~/.local/share/portmap')

# Fetch/update from Wikipedia (only if stale)
records = pm.update()

# Force a fresh pull
records = pm.update(force=True)

# Load cached data without hitting the network
records = pm.load()

# Look up specific ports — returns matching record dicts
results = pm.lookup(80, 443, 6667)

# Search descriptions by keyword
results = pm.search('minecraft')

# Fetch the last year of revision history
revisions = pm.history(days=365)
```

Every method returns plain `list[dict]` values you can work with directly:

```python
for rec in pm.lookup(22, 80):
    port = rec['port']          # int or "start-end" str
    for svc in rec['services']:
        print(port, svc['tcp'], svc['udp'], svc['description'])
```

## CLI Usage

| Flag               | Description                                  |
|:-------------------|:---------------------------------------------|
| `ports`            | Comma-separated port numbers to look up      |
| `-s TERM`          | Search descriptions for a keyword            |
| `-j`               | Output as NDJSON *(pipeable to `jq`)*        |
| `-md`              | Output as Markdown *(ports + history)*       |
| `-u`               | Force update from Wikipedia                  |
| `-d`               | Enable debug logging                         |
| `--data-dir DIR`   | Directory for data files *(default: `.`)*    |
| `--history [DAYS]` | Fetch revision history *(default: 365 days)* |
| `--serve`          | Start the JSON API server                    |
| `--host ADDR`      | API bind address *(default: `127.0.0.1`)*    |
| `--port PORT`      | API bind port *(default: `6660`)*            |

## Examples

```bash
# Look up ports
portmap 80,443,6667

# Search for a keyword
portmap -s irc

# NDJSON output (pipe to jq)
portmap 80,443 -j

# Store data in a custom directory
portmap -u --data-dir ~/.local/share/portmap

# Fetch revision history
portmap --history 365

# Start the API server
portmap --serve

# Bind to a specific address and port
portmap --serve --host 0.0.0.0 --port 8080
```

## API Server

Start with `portmap --serve`. Binds to `127.0.0.1:6660` by default.

| Endpoint            | Description                                          |
|:--------------------|:-----------------------------------------------------|
| `GET /`             | API info and available endpoints                     |
| `GET /ports`        | All ports *(query: `?search=TERM&limit=N&offset=N`)* |
| `GET /ports/80,443` | Lookup specific ports *(comma-separated, 0–65535)*   |
| `GET /history`      | Revision history *(query: `?limit=N&offset=N`)*      |

```bash
curl -s localhost:6660/ports/22,80 | jq .
curl -s 'localhost:6660/ports?search=irc&limit=10' | jq .
curl -s 'localhost:6660/history?limit=5' | jq .
```

###### Output
```
PORT        TCP         UDP         SCTP        DCCP        DESCRIPTION
────────────────────────────────────────────────────────────────────────
80          Yes         Yes         Yes         --          Hypertext Transfer Protocol (HTTP) uses TCP in versions 1.x and 2.
443         Yes         Yes         Yes         --          Hypertext Transfer Protocol Secure (HTTPS) uses TCP in versions 1.x and 2.
6665-6669   Yes         --          --          --          Internet Relay Chat (IRC)
```

---

###### Mirrors: [SuperNETs](https://git.supernets.org/acidvegas/portmap) • [GitHub](https://github.com/acidvegas/portmap) • [GitLab](https://gitlab.com/acidvegas/portmap) • [Codeberg](https://codeberg.org/acidvegas/portmap)
