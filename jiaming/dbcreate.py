import sqlite3 as sqlite

conn = sqlite.connect("database.db")
connection.execute('CREATE TABLE IF NOT EXISTS users(username TEXT PRIMARY KEY, password TEXT);')
