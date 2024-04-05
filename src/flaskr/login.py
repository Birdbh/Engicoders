from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

from flask import flash
from flaskr.db import get_db
from flask_login import login_user
from flaskr.user import User, SuperUser
from hashlib import sha512

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
                    hasher = sha512()
                    hasher.update(password.encode())
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
