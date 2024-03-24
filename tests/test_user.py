import pytest
import sys
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from flask import Flask, render_template
sys.path.append("src")
import flaskr.register as register

import flaskr.db as dbClass
import flaskr.user as Userclass



def test_register(app):
    with app.test_request_context():
        user = Userclass.User()
        user.register("test")
        assert user.get_id() == 1
        assert user.get_username() == 'test'
