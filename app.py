from flask import Flask, render_template, redirect,url_for, request
from flask_bootstrap import Bootstrap5
from add_book_form import BookForm
from flask_font_awesome import FontAwesome
from flask_mysqldb import MySQL
from termcolor import colored

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
            'id': row['id'],
            'name': row['bookname'],
            'year': row['bookyear'],
            'author': row['author_name'],
            'description': row['bookdescription'],
            'image_url': row['image_url'],
            'wikipedia_url': row['link']
        }
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
        book_name = str(form.book_name.data).replace("'", "\\'")
        book_year = form.book_year.data
        author_name = str(form.author_name.data).replace("'", "\\'")
        wikipedia_link = form.wikipedia_link.data
        book_description = str(form.book_description.data).replace("'", "\\'")
        image_url = form.image_url.data
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        print(colored('|QUESTO è CIO CHE VIENE INSERITO|', 'red'))
        print(f"INSERT INTO `library`.`book` (`bookname`, `author_name`, `bookyear`, `link`, `bookdescription`, `image_url`) VALUES ('{book_name}', '{author_name}', '{book_year}', '{wikipedia_link}', '{book_description}', '{image_url}');")
        cursor.execute(f"INSERT INTO `library`.`book` (`bookname`, `author_name`, `bookyear`, `link`, `bookdescription`, `image_url`) VALUES ('{book_name}', '{author_name}', '{book_year}', '{wikipedia_link}', '{book_description}', '{image_url}');")
        mysql.connection.commit()
        return redirect(url_for('index'))
    return render_template('add.html', form=form)

@app.route("/delete")
def delete():
    book_id = request.args.get('id')
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute(f"DELETE FROM `library`.`book` WHERE (`id` = '{book_id}');")
    mysql.connection.commit()

    print(book_id)
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)