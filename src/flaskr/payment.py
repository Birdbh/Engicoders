from flaskr.db import get_db
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from flask import Flask, render_template, flash
from flaskr.db import get_db
from flaskr.user import User
from flask_login import login_user


class PaymentForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])

class Payment():
    cardNumber = ""


    def commitToDatabase():
        db = get_db()
        
