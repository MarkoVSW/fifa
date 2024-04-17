import pandas as pd
import os

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

def update(df):
    df.drop(columns=["Unnamed: 0"], inplace=True)
    df = df.sort_values(by='POINTS', ascending=False)
    markdown_table = df.to_markdown()

    # Write markdown table to README.md file
    with open('README.md', 'w') as readme_file:
        readme_file.write(markdown_table)

def load_df():
    file_path = 'table.csv'
    if os.path.exists(file_path):
        df = pd.read_csv("table.csv")
    else:
        create()
        df = pd.read_csv("table.csv")
    return df

def readme_main():
    df = load_df()
    update(df)

if __name__ == "__main__":
    readme_main()