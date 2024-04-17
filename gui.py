from tkinter import *
import pandas as pd
from pandastable import Table, TableModel

class TestApp(Frame):
    """Basic test frame for the table"""
    def __init__(self, parent=None):
        self.parent = parent
        Frame.__init__(self)
        self.main = self.master
        self.main.geometry('1000x200+200+200')
        self.main.title('Fifa Table')
        f = Frame(self.main)
        f.pack(fill=BOTH,expand=1)
        df = pd.read_csv("table.csv")
        df = df.sort_values(by='POINTS', ascending=False)
        self.table = pt = Table(f, dataframe=df,
                                showtoolbar=True, showstatusbar=True)
        pt.show()

if __name__ == "__main__":
    app = TestApp()
    app.mainloop()