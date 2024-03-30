import pytest
import sys
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from flask import Flask, render_template
import flask_login
sys.path.append("src")
import flaskr.register as register
from flask_login import current_user, logout_user
import flaskr.login as login

import flaskr.db as dbClass
import flaskr.user as UserClass
import flaskr.upgrade as upgrade
from hashlib import sha512



def test_upgrade(app):
     with app.test_request_context():
        form = register.RegistrationForm()
        form.register("TestUser2", "Test2", "Test2")
        user = flask_login.current_user
        upgrade.upgrade()
        assert not user.get_password() == "Test2"
        hasher = sha512()
        hasher.update(str.encode("Test2"))
        assert user.get_password() == hasher.hexdigest()

        