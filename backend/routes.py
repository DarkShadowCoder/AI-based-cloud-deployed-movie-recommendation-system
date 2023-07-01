""""
Fichier principal du programme
"""
# import main Flask class and request object
from flask import Flask , flash, render_template , request , url_for ,jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.secret_key = 'many random bytes'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'movieadviserdatabase'

mysql = MySQL(app)

@app.route('/')
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM user')
    data = cur.fetchall()
    cur.close()
    return render_template('helloreact/public/index.html', users=data)

if __name__=='__main__':
    app.run()