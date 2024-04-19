|    | PLAYERS       |   PLAYED |   WINS |   DRAWS |   LOSSES |   SCORED |   CONCEDED |   POINTS |
|---:|:--------------|---------:|-------:|--------:|---------:|---------:|-----------:|---------:|
|  0 | Marko Raseta  |       16 |      8 |       5 |        3 |       36 |         26 |       29 |
|  1 | Stefan Micic  |       17 |      6 |       3 |        8 |       22 |         26 |       21 |
|  2 | Marko Vasilic |       17 |      5 |       4 |        8 |       29 |         32 |       19 |
## How to Run

To add a new result to the table:

```bash
python fifa.py new
```

To reset the tables:

```bash
python fifa.py reset
```

To append history to the table:

```bash
python fifa.py append_history [start]
```

- `start`: int, optional. The index from which to start appending historical data. Default is 0.
        