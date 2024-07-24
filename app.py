from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_font_awesome import FontAwesome
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)
bootstrap = Bootstrap5(app)
font_awesome = FontAwesome(app)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'library'
mysql = MySQL(app)

# with app.app_context():
#     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     cursor.execute('SELECT * FROM library.book;')
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row['bookname'])

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def add_book():
    return render_template('add.html')

@app.route('/test', methods=['GET'])
def testing():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM library.book;')
    rows = cursor.fetchall()
    books = []
    for row in rows:
        books.append(row['bookname'])
        print(row['bookname'])
    
    print(books)
    return render_template('test.html', books = books)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
