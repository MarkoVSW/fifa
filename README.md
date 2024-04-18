|    | PLAYERS       |   PLAYED |   WINS |   DRAWS |   LOSSES |   SCORED |   CONCEDED |   POINTS |
|---:|:--------------|---------:|-------:|--------:|---------:|---------:|-----------:|---------:|
|  0 | Marko Raseta  |       14 |      7 |       4 |        3 |       33 |         24 |       25 |
|  2 | Stefan Micic  |       15 |      6 |       1 |        8 |       19 |         23 |       19 |
|  1 | Marko Vasilic |       15 |      5 |       3 |        7 |       26 |         28 |       18 |
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
        