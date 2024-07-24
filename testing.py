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
#     arr = []
#     books = {}
#     for row in rows:
#         # print(f"SELECT author_name FROM library.book, library.author WHERE book.authorID = author.id AND bookname = {row['bookname']}")
#         cursor.execute(f"SELECT author_name FROM library.book, library.author WHERE book.authorID = author.id AND bookname = '{row['bookname']}'")
#         author_name = cursor.fetchone()
#         books = {
#             'name': row['bookname'],
#             'year': row['bookyear'],
#             'author': author_name['author_name'],
#             'description': row['desc']
#         }
#         arr.append(books)
#         # print(author_name)
#     for i in arr:
#         print(i)

with app.app_context():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("INSERT INTO `library`.`book` (`bookname`, `author_name`, `bookyear`, `link`, `bookdescription`) VALUES ('prova Libro aggiunto da python 22', 'Python2', '2023', '', '');")
    mysql.connection.commit()