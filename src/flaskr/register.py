from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from flask import Flask, render_template
from flaskr.db import get_db

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_user(self, username):
        if(len(username) > 0):
            self.username = username
            return True

    def validate_pass(self, password, password2):
        if(password == password2):
            self.password = password
            return True
    def register(self, username, password, password2): 
        db = get_db()
        if(self.validate_user(username) and (self.validate_pass(password, password2))):
            db.execute("INSERT INTO user (Username, Password) values (?,?)", (username, password))
            db.commit()
            return True
        return False

