|    | PLAYERS       |   PLAYED |   WINS |   DRAWS |   LOSSES |   SCORED |   CONCEDED |   POINTS |
|---:|:--------------|---------:|-------:|--------:|---------:|---------:|-----------:|---------:|
|  0 | Marko Raseta  |       16 |      8 |       5 |        3 |       36 |         26 |       29 |
|  1 | Stefan Micic  |       16 |      6 |       2 |        8 |       20 |         24 |       20 |
|  2 | Marko Vasilic |       16 |      5 |       3 |        8 |       27 |         30 |       18 |
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
        