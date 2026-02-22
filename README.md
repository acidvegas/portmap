# portmap

Scrape the [Wikipedia list of TCP/UDP port numbers](https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers) into a local NDJSON database with revision tracking. Only fetches from Wikipedia when the article has actually changed.

## Usage

| Flag               | Description                                  |
|:-------------------|:---------------------------------------------|
| `ports`            | Comma-separated port numbers to look up      |
| `-s TERM`          | Search descriptions for a keyword            |
| `-j`               | Output as NDJSON *(pipeable to `jq`)*        |
| `-md`              | Output as Markdown *(ports + history)*       |
| `-u`               | Force update from Wikipedia                  |
| `-d`               | Enable debug logging                         |
| `--history [DAYS]` | Fetch revision history *(default: 365 days)* |

## Examples

###### Command:
```bash
python3 portmap.py 80,443,6667
```

###### Output:
```
PORT        TCP         UDP         SCTP        DCCP        DESCRIPTION
────────────────────────────────────────────────────────────────────────
80          Yes         Yes         Yes         --          Hypertext Transfer Protocol (HTTP) uses TCP in versions 1.x and 2.
443         Yes         Yes         Yes         --          Hypertext Transfer Protocol Secure (HTTPS) uses TCP in versions 1.x and 2.
6665-6669   Yes         --          --          --          Internet Relay Chat (IRC)
```


###### Command:
```
python3 portmap.py 80,443,6667 -j
```

###### Output
```json
{"port": 80, "services": [{"tcp": true, "udp": true, "sctp": true, "dccp": false, "description": "Hypertext Transfer Protocol (HTTP)..."}]}
{"port": 443, "services": [{"tcp": true, "udp": true, "sctp": true, "dccp": false, "description": "Hypertext Transfer Protocol Secure (HTTPS)..."}]}
{"port": "6665-6669", "services": [{"tcp": true, "udp": false, "sctp": false, "dccp": false, "description": "Internet Relay Chat (IRC)"}]}
```

---

###### Mirrors: [SuperNETs](https://git.supernets.org/acidvegas/portmap) • [GitHub](https://github.com/acidvegas/portmap) • [GitLab](https://gitlab.com/acidvegas/portmap) • [Codeberg](https://codeberg.org/acidvegas/portmap)