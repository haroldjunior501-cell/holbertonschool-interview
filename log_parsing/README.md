# Log Parsing

Read log lines from stdin and compute HTTP metrics.

## Description

The script parses lines with this format:

`<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>`

Every 10 lines read from stdin, and on keyboard interruption (`CTRL + C`), it prints:

- Total file size: `File size: <total size>`
- Status code counts in ascending order: `<status code>: <number>`

Tracked status codes: 200, 301, 400, 401, 403, 404, 405 and 500.

## Files

| File | Description |
|------|-------------|
| `0-stats.py` | Parses stdin and prints log statistics |

## Usage

```bash
./0-generator.py | ./0-stats.py
```
