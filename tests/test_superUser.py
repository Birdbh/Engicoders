import pytest
import sys
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from flask import Flask, render_template
sys.path.append("src")
import flaskr.register as register
from flask_login import current_user, logout_user
import flaskr.login as login

import flaskr.db as dbClass
import flaskr.user as UserClass
from hashlib import sha512



def test_hash_password(app):
     with app.test_request_context():
        form = register.RegistrationForm()
        form.register("TestUser", "Test", "Test")
        db = dbClass.get_db()
        user = UserClass.SuperUser(username="TestUser", password="Test")
        user.upgrade()
        assert not user.get_password() == "Test"
        hasher = sha512()
        hasher.update(str.encode("Test"))
        assert user.get_password() == hasher.hexdigest()

def test_logging_in(app):
   with app.test_request_context():
        user2 = UserClass.SuperUser(username="test2")
        user2.upgrade()
        loginForm = login.LoginForm()
        assert loginForm.login("test2", 'test')
        assert current_user.is_authenticated
        logout_user()
        assert not current_user.is_authenticated
        assert current_user.is_anonymous

        