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

def createBooksDict():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM library.book;')
    rows = cursor.fetchall()
    booksArray = []
    book = {}
    for row in rows:
        cursor.execute(f"SELECT author_name FROM library.book, library.author WHERE book.authorID = author.id AND bookname = '{row['bookname']}'")
        author_name = cursor.fetchone()
        book = {
            'name': row['bookname'],
            'year': row['bookyear'],
            'author': author_name['author_name'],
            'description': row['bookdescription'],
            'image_url': row['image_url'],
            'wikipedia_url': row['link']
        }
        print(row['image_url'])
        booksArray.append(book)

    return booksArray

# with app.app_context():
#     cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
#     cursor.execute('SELECT * FROM library.book;')
#     rows = cursor.fetchall()
#     for row in rows:
#         print(row['bookname'])

@app.route('/')
def index():
    return render_template('index.html', books = createBooksDict())

@app.route('/add')
def add_book():
    return render_template('add.html')

@app.route('/test', methods=['GET'])
def testing():
    return render_template('test.html', books = createBooksDict())

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)



