import pandas as pd
import os
import argparse

class FifaTable:
    def __init__(self, table_name, history_table_name):
        self.table_name = table_name
        self.history_table_name = history_table_name
        self.table = self.create_table()
        self.history_table = self.create_history_table()

    def create_table(self):
        if os.path.exists(self.table_name):
            df = pd.read_csv(self.table_name)
        else:
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
            df = pd.DataFrame(data, index=[0, 1, 2])
            df.to_csv(self.table_name)
        return df
    
    def create_history_table(self):
        if os.path.exists(self.history_table_name):
            df = pd.read_csv(self.history_table_name)
        else:
            columns = ['PLAYER_1', 'PLAYER_2', 'GOALS_1', 'GOALS_2']
            df = pd.DataFrame(columns=columns)
            df.to_csv(self.history_table_name)
        return df
    
    def update_table(self, player1, player2, goals1, goals2):
        name_mapping = {
            "SM": self.table.index[self.table['PLAYERS'] == 'Stefan Micic'].tolist()[0], 
            "MR": self.table.index[self.table['PLAYERS'] == 'Marko Raseta'].tolist()[0],
            "MV" : self.table.index[self.table['PLAYERS'] == 'Marko Vasilic'].tolist()[0]
        }
        player1 = name_mapping[player1]
        player2 = name_mapping[player2]
        print
        self.table.at[player1, 'SCORED'] += goals1
        self.table.at[player1, 'CONCEDED'] += goals2
        self.table.at[player2, 'SCORED'] += goals2
        self.table.at[player2, 'CONCEDED'] += goals1
        self.table.at[player1, 'PLAYED'] += 1
        self.table.at[player2, 'PLAYED'] += 1
        
        if goals1 > goals2:
            self.table.at[player1, 'WINS'] += 1
            self.table.at[player2, 'LOSSES'] += 1
        elif goals1 < goals2:
            self.table.at[player1, 'LOSSES'] += 1
            self.table.at[player2, 'WINS'] += 1
        else:
            self.table.at[player1, 'DRAWS'] += 1
            self.table.at[player2, 'DRAWS'] += 1
            
        self.table['POINTS'] = self.table['WINS']*3 + self.table['DRAWS']
        if "Unnamed: 0" in self.table.columns:
            self.table.drop(columns=["Unnamed: 0"], inplace=True)
        self.table = self.table.sort_values(by='POINTS', ascending=False)
        self.table.to_csv(self.table_name)
        self.update_readme()

    def update_history_table(self, player1, player2, goals1, goals2):
        if "Unnamed: 0" in self.history_table.columns:
            self.history_table.drop(columns=["Unnamed: 0"], inplace=True)
        self.history_table.loc[len(self.history_table.index)] = [player1, player2, goals1, goals2]  
        self.history_table.to_csv(self.history_table_name)

    def read_new_result(self):
        while True:
            print("Enter 'exit' to quit.")
            player1 = input("Enter player one's name (SM/MR/MV): ").upper()
            if player1 == 'exit':
                break
            while player1 not in ('SM', 'MR', 'MV'):
                print("Invalid player name. Please enter SM, MR, or MV.")
                player1 = input("Enter player one's name (SM/MR/MV): ").upper()
                if player1 == 'exit':
                    break
            if player1 == 'exit':
                break

            goals1 = -1
            while goals1 < 0:
                goals1_str = input("Enter the number of goals scored by player one: ")
                if goals1_str.lower() == 'exit':
                    break
                try:
                    goals1 = int(goals1_str)
                    if goals1 < 0:
                        print("Number of goals must be non-negative.")
                except ValueError:
                    print("Invalid input. Please enter a non-negative integer.")
            if goals1 == 'exit':
                break

            player2 = input("Enter player two's name (SM/MR/MV): ").upper()
            if player2 == 'exit':
                break
            while player2 not in ('SM', 'MR', 'MV') or player2 == player1:
                if player2 == player1:
                    print("Player two cannot have the same name as player one.")
                else:
                    print("Invalid player name. Please enter SM, MR, or MV.")
                player2 = input("Enter player two's name (SM/MR/MV): ").upper()
                if player2 == 'exit':
                    break
            if player2 == 'exit':
                break

            goals2 = -1
            while goals2 < 0:
                goals2_str = input("Enter the number of goals scored by player two: ")
                if goals2_str.lower() == 'exit':
                    break
                try:
                    goals2 = int(goals2_str)
                    if goals2 < 0:
                        print("Number of goals must be non-negative.")
                except ValueError:
                    print("Invalid input. Please enter a non-negative integer.")
            if goals2 == 'exit':
                break

            to_save = input("Write 'y' to save results to table: ")
            if to_save == 'y':
                self.update_table(player1, player2, goals1, goals2)
                self.update_history_table(player1, player2, goals1, goals2)
            break

    def reset_tables(self):
        os.remove(self.table_name)
        os.remove(self.history_table_name)
        self.table = self.create_table()
        self.history_table = self.create_history_table()
        self.update_readme()

    def append_history_to_table(self, start=0):
        df = self.history_table.iloc[start:]
        for index, row in df.iterrows():
            self.update_table(row['PLAYER_1'], row['PLAYER_2'], row['GOALS_1'], row['GOALS_2'])

    def update_readme(self):
        markdown_table = self.table.to_markdown()
        instructions = """
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
        """

        # Write markdown table and instructions to README.md
        with open('README.md', 'w') as readme_file:
            readme_file.write(markdown_table)
            readme_file.write(instructions)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="FIFA Table Management")

    # Add arguments
    parser.add_argument('action', choices=['new', 'reset', 'append_history'], help="Action to perform")
    parser.add_argument('start', type=int, nargs='?', default=0, help="Starting index for appending history")

    args = parser.parse_args()

    fifa = FifaTable('table.csv', 'history_table.csv')

    if args.action == 'new':
        fifa.read_new_result()
    elif args.action == 'reset':
        fifa.reset_tables()
    elif args.action == 'append_history':
        fifa.append_history_to_table(args.start)