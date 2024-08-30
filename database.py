from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

# create a Flask Instance
app = Flask(__name__)
app.url_map.strict_slashes = False
#add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'

db = SQLAlchemy(app)

# create a route decorator
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/solution2')
def solution2():
    return render_template('solution2.html')

@app.route('/solution3')
def solution3():
    return render_template('solution3.html')


if __name__ == '__main__':
    app.run(host="localhost", port=5000, debug=True)
