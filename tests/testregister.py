from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from flask import Flask, render_template
import src.flaskr.register as register


app = Flask(__name__,template_folder='templates')
app.config['SECRET_KEY'] = SECRET_KEY='test_change_later'
@app.route('/')

def index(): 
    form = register.RegistrationForm()
    return render_template('register.html', form = form)

if __name__ == '__main__': 
    app.run() 