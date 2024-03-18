
from flask import render_template
from flaskr import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')

