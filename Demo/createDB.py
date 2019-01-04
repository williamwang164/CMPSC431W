import sqlite3 as sqlite
import pandas as pd

dataFile = pd.read_csv('Students.csv')
colNames = list(dataFile.columns.values)
print(type(colNames))

conn = sqlite.connect('database.db')
conn.text_factory = str
dataFile.to_sql("Students", conn, index = False, if_exists='replace')
