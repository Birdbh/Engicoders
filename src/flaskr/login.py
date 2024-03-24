from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from flask import Flask, render_template, flash
from flaskr.db import get_db
from flask_login import login_user
from flaskr.user import User

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    
    def login(self, username, password):
        db = get_db()
        try:
            if(db.execute("SELECT password from user where username = (?)", (username,)).fetchone()['password'] == password):
                user = User(username=username)
                login_user(user, True)
                return True
            flash('Username or Password is incorrect')
        except:
            flash('Username does not exist!')
        return False
