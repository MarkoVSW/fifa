|    | PLAYERS       |   PLAYED |   WINS |   DRAWS |   LOSSES |   SCORED |   CONCEDED |   POINTS |
|---:|:--------------|---------:|-------:|--------:|---------:|---------:|-----------:|---------:|
|  0 | Marko Raseta  |       18 |     10 |       5 |        3 |       39 |         27 |       35 |
|  1 | Stefan Micic  |       18 |      6 |       3 |        9 |       22 |         27 |       21 |
|  2 | Marko Vasilic |       18 |      5 |       4 |        9 |       30 |         34 |       19 |
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
        