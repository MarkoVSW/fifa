import pandas as pd

def create():
    # Create a dictionary with initial values
    data = {
        'PLAYERS': ['Stefan Micic', 'Marko Raseta', 'Marko Vasilic'],
        'PLAYED': [14, 14, 14],
        'WINS': [5, 7, 5],
        'DRAWS': [1, 4, 3],
        'LOSSES': [8, 3, 6],
        'SCORED': [18, 33, 26],
        'CONCEDED': [23, 24, 27],
        'POINTS': [16, 25, 18]
    }

    # Create DataFrame
    df = pd.DataFrame(data, index=[0, 1, 2])
    df.to_csv("table.csv")

if __name__ == "__main__":
    create()
