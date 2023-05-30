import pandas as pd

#Table representing class that contains a modifiable table that will always be rectangular.
# Empty or missing slots within the table are filled in with a default value
class Table:
    def __init__(self):
        self.rows = 0
        self.columns = 0
        self.table = dict()
    
    def shape(self)->tuple: return (self.rows, self.columns)

    def row(self, index)->dict: 
        return {col : values[index] for col, values in self.table.items()}

    def col(self, index)->list:
        return self.table[index]
    
    def cell(self, row, col):
        return self.col(col)[row]

    def append_row(self, row, index=-1)->None:
        index = self.rows if index == -1 else index
        for i in self.table:
            self.table[i].insert(index, type(self.table[i][0])())
        for i in row.keys():
            val = row[i]
            if i not in self.table.keys():
                self.table[i] = [type(val)() for _ in range(index)]
                self.table[i].append(val)
                self.table[i] += [type(val)() for _ in range(self.rows - index)]
            else:
                self.table[i][index] = val
        self.rows += 1
    
    def append_col(self, col, index=-1)->None:
        index = len(self.table) if index == -1 else index
        if len(col[1]) > self.rows:
            self.rows = len(col[1])
            for i in self.table:
                dtype = type(self.table[i][0])
                while len(self.table[i]) < self.rows:
                    self.table[i] += [dtype()]
        elif len(col[1]) < self.rows:
            dtype = type(col[1][0])()
            while len(col[1]) < self.rows:
                col[1] += [dtype()]
        self.table = [(key, value) for key, value in self.table.items()]
        self.table.insert(index, col)
        self.table = {key: value for key, value in self.table}
        self.columns += 1

    def to_DataFrame(self)->pd.DataFrame:
        return pd.DataFrame(self.table)
