import pytest
import sys
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from flask import Flask, render_template
sys.path.append("src")
import flaskr.register as register
import flaskr.db as dbClass



# app = Flask(__name__,template_folder='templates')
# app.config['SECRET_KEY'] = SECRET_KEY='test_change_later'
# @app.route('/')

# def index(): 
#     form = register.RegistrationForm()
#     return render_template('register.html', form = form)

def test_register(app):
    with app.app_context:
        register.RegistrationForm.register("Username", "Test", "Test")
        db = dbClass.get_db()
        assert db.execute("SELECT username from user") == "Username"




# if __name__ == '__main__': 
#     app.run() 