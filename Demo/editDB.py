# -*- coding: utf-8 -*-
from flask import *
import pandas as pd
import sqlite3 as sqlite
import createDB
app = Flask(__name__)
host = 'http://127.0.0.1:5000/'

@app.route('/', methods=['POST', 'GET'])
def index():
    dbConnection = sqlite.connect('database.db')
    cursor = dbConnection.cursor()
    if request.method == 'POST':
        sort = request.form['sortBy']
        print(sort)
        cursor.execute('SELECT * FROM Students ORDER BY "' + sort + '" ASC;')
        result = cursor.fetchall()
        return render_template('edit.html', headers= createDB.colNames, data=result)
    return render_template('edit.html')



if __name__ == '__main__':
   app.run(debug = True)
