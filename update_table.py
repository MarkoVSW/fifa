import pandas as pd
from gui import TestApp
from update_readme import readme_main

def update_dataframe(df, player1, goals1, player2, goals2):
    name_mapping = {"SM": 0, "MR": 1, "MV" : 2}
    player1 = name_mapping[player1]
    player2 = name_mapping[player2]
    # Update goals scored and conceded
    df.at[player1, 'SCORED'] += goals1
    df.at[player1, 'CONCEDED'] += goals2
    df.at[player2, 'SCORED'] += goals2
    df.at[player2, 'CONCEDED'] += goals1
    df.at[player1, 'PLAYED'] += 1
    df.at[player2, 'PLAYED'] += 1
    
    # Update wins, draws, losses, and points
    if goals1 > goals2:
        df.at[player1, 'WINS'] += 1
        df.at[player2, 'LOSSES'] += 1
    elif goals1 < goals2:
        df.at[player1, 'LOSSES'] += 1
        df.at[player2, 'WINS'] += 1
    else:
        df.at[player1, 'DRAWS'] += 1
        df.at[player2, 'DRAWS'] += 1
        
    # Update points
    df['POINTS'] = df['WINS']*3 + df['DRAWS']
    df.drop(columns=["Unnamed: 0"], inplace=True)
    df.to_csv('table.csv')
    

def main():
    df = pd.read_csv('table.csv')
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

        update_dataframe(df, player1, goals1, player2, goals2)
        break

    readme_main()


if __name__ == "__main__":
    main()