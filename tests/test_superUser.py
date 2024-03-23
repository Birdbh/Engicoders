import pytest
import sys
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from flask import Flask, render_template
sys.path.append("src")
import flaskr.register as register

import flaskr.db as dbClass
import flaskr.user as UserClass
from hashlib import sha256



def test_hash_password(app):
     with app.test_request_context():
        form = register.RegistrationForm()
        form.register("TestUser", "Test", "Test")
        db = dbClass.get_db()
        user = UserClass.SuperUser(username="TestUser", password="Test")
        assert not user.get_password() == "test"
        hasher = sha256()
        hasher.update(str.encode("Test"))
        assert user.get_password() == hasher.hexdigest()

        