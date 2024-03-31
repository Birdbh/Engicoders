from flaskr.db import get_db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from flask import Flask, render_template, flash
from flaskr.db import get_db
from flaskr.user import User
from flask_login import login_user


class PaymentForm(FlaskForm):
    CreditCard = IntegerField('Credit Card Number', validators=[DataRequired()])
    ExpirationDate = DateField('Expiration Date', format='%Y-%m')
    CardName = StringField('Name on Card', validators=[DataRequired()])
    SecurityDigits = IntegerField('Credit Card Number', validators=[DataRequired()])
    submit = SubmitField('Upgrade!')

    def validate_cardNumber(self, CreditCard):
        
        return True

    def validate_pass(self, password, password2):
        if(password == password2):
            self.password = password
            return True
    def pay(self, username, password, password2): 
        db = get_db()
        if(self.validate_user(db, username) and (self.validate_pass(password, password2))):
            db.execute("INSERT INTO user (Username, Password) values (?,?)", (username, password))
            db.commit()
            user = User(username=username)
            login_user(user, True)
            return True
        return False

class Payment():
    cardNumber = ""


    def commitToDatabase():
        db = get_db()
        
