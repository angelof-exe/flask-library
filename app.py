from flask import Flask, render_template
from flask_bootstrap import Bootstrap5
from flask_font_awesome import FontAwesome

app = Flask(__name__)
bootstrap = Bootstrap5(app)
font_awesome = FontAwesome(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add')
def add_book():
    return render_template('add.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
