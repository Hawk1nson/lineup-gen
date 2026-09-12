# lineup-gen

A small Python CLI tool that generates randomized batting orders for a little league baseball team — with constraint checking so certain players don't end up back-to-back in the order.

Built for my son's team to take the guesswork (and the arguing) out of setting a lineup before each game.

> **Note:** the player names in this repo are placeholders, not the real kids on the team.

## Why it exists

Setting a batting order by hand every game gets tedious, and "random" done by a human isn't really random. This script handles it in a few seconds — and enforces the real-world coaching rules that a plain shuffle can't.

## Features

- **Randomized lineup generation** — a fresh, genuinely random order every run
- **Forbidden pair constraints** — certain players are never placed back-to-back in the order (defined in `forbidden_pairs`)
- **Handles absences** — prompts for how many players are out and which ones, then builds the lineup from who's actually available
- **Reshuffle loop** — don't like the result? Press `r` for a new one before committing
- **CSV export** — accepted lineups are written to `lineup.csv` for printing or sharing

## Usage

```bash
python3 lineup_gen.py
```

The script walks you through it:

1. Enter how many players aren't playing (`0`–`10`, or `x` to quit)
2. Enter the initials of each absent player
3. Review the generated lineup
4. Choose: `y` to accept and export, `r` to reshuffle, `x` to quit

Example output:

```
✅ Valid Batting Lineup:
1. Logan Hughes (LH)
2. Caleb Brown (CB)
3. Isaac Parker (IP)
...
```

## Configuring for your own team

Two things to edit at the top of `lineup_gen.py`:

- **`players_dict`** — maps player initials to full names. Replace with your roster.
- **`forbidden_pairs`** — tuples of initials that shouldn't bat consecutively. Leave it as an empty list if you don't need this.

## Requirements

- Python 3
- No external dependencies — standard library only (`random`, `csv`)

## Possible future improvements

- Load roster and constraints from a config file instead of hardcoding
- Track lineups across games so batting positions rotate fairly over a season
- Fielding position assignment
