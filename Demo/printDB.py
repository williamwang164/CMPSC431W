# -*- coding: utf-8 -*-
from flask import *
import pandas as pd
import sqlite3 as sqlite
import createDB
app = Flask(__name__)

@app.route('/')
def index():
    dbConnection = sqlite.connect('database.db')
    cursor = dbConnection.cursor()
    cursor.execute('SELECT * FROM Students ORDER BY Id ASC;')
    result = cursor.fetchall()
    return render_template('table.html', headers= createDB.colNames, data=result)
if __name__ == '__main__':
   app.run(debug = True)
