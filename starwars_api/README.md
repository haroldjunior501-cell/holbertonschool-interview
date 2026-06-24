# Star Wars API

Print all characters from a Star Wars movie using the SWAPI.

## Description

The script takes a movie ID as the first argument and prints each character
name on its own line, in the same order as the `characters` list from the
`/films/` endpoint.

## Requirements

- Node.js 10.x
- `request` module

## Files

| File | Description |
|------|-------------|
| `0-starwars_characters.js` | Prints characters for a given film ID |

## Usage

```bash
./0-starwars_characters.js 3
```

Example output for movie ID `3` (Return of the Jedi):

```
Luke Skywalker
C-3PO
R2-D2
...
```
