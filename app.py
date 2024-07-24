from flask import Flask, render_template, redirect,url_for
from flask_bootstrap import Bootstrap5
from add_book_form import BookForm
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
app.secret_key = 'blablablabla'
mysql = MySQL(app)

def createBooksDict():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT * FROM library.book;')
    rows = cursor.fetchall()
    booksArray = []
    book = {}
    for row in rows:
        author_name = cursor.fetchone()
        book = {
            'name': row['bookname'],
            'year': row['bookyear'],
            'author': row['author_name'],
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


@app.route('/test', methods=['GET'])
def testing():
    return render_template('test.html', books = createBooksDict())

@app.route('/add', methods=["GET", "POST"])
def add_book():
    form = BookForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('add.html', form=form)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)