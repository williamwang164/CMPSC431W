from flask import Flask, render_template, request
import sqlite3 as sql

connection = sql.connect('database.db')
connection.execute('CREATE TABLE IF NOT EXISTS users(username TEXT PRIMARY KEY, password TEXT);')



app = Flask(__name__)

host = 'http://127.0.0.1:5000/'

@app.route('/', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        result = valid_login(request.form['username'],
                       request.form['password'])
        if result:
            return render_template('login.html', error=error, url=host, result=result)
        else:
            error = 'invalid user input'

    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error, url=host)

def authorizer(action, arg1, arg2, db_name, trigger_name):
    if action == SQLITE_DELETE and arg1 == 'users':
        return SQLITE_DENY  # 1
    elif action == SQLITE_READ and arg1 == 'users' and arg2 == 'password':
        return SQLITE_IGNORE  # 2
    return SQLITE_OK  # 0

def valid_login(username, password):
    connection = sql.connect('database.db')
    connection.execute('INSERT INTO users (username, password) VALUES (?,?);', (username, password))
    connection.commit()
    cursor = connection.execute('SELECT * FROM users;')
    return cursor.fetchall()
