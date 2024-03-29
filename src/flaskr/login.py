from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from flask import Flask, render_template, flash
from flaskr.db import get_db
from flask_login import login_user
from flaskr.user import User, SuperUser
from hashlib import sha256

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
    
    def login(self, username, password: str):
        db = get_db()
        try:
            userid = db.execute("SELECT id from user where username = (?)", (username,)).fetchone()['id']
            try:
                if(db.execute("SELECT userid from PremiumUser where userid = (?)", (userid,)).fetchone()['userid'] == userid):
                    hasher = sha256()
                    hexer = ""
                    for character in password:
                        print(character, character.encode('utf-8').hex())
                        hexer += character
                    hasher.update(hexer.encode())
                    password = hasher.hexdigest()
                    pass2 = db.execute("SELECT password from user where username = (?)", (username,)).fetchone()['password'] 
                    
                    if(db.execute("SELECT password from user where username = (?)", (username,)).fetchone()['password'] == password):
                        user = SuperUser(username=username, userid=userid)
                        login_user(user, True)
                        return True
                    flash('Username or Password is incorrect')
            except Exception as a:
                exceptionError = a
        except:
            pass
        try:
            if(db.execute("SELECT password from user where username = (?)", (username,)).fetchone()['password'] == password):
                user = User(username=username)
                login_user(user, True)
                return True
            flash('Username or Password is incorrect')
        except:
            flash('Username does not exist!')
        return False
