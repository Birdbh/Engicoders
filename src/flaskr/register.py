from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from flask import Flask, render_template, flash
from flaskr.db import get_db
from flaskr.user import User
from flask_login import login_user

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_user(self, db, username):
        for x in db.execute("SELECT username from user").fetchall():
            if username in x['username']:
                flash('Username already taken')
                return False
        if(len(username) > 0):
            self.username = username
            return True

    def validate_pass(self, password, password2):
        if(password == password2):
            self.password = password
            return True
    def register(self, username, password, password2): 
        db = get_db()
        if(self.validate_user(db, username) and (self.validate_pass(password, password2))):
            db.execute("INSERT INTO user (Username, Password) values (?,?)", (username, password))
            db.commit()
            user = User(username=username)
            login_user(user, True)
            return True
        return False

