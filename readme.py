import pandas as pd
import os
from create_table import create

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