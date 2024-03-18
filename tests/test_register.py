import pytest
import sys
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from flask import Flask, render_template
sys.path.append("src")
import flaskr.register as register

import flaskr.db as dbClass




def test_register(app):
    with app.test_request_context():
        form = register.RegistrationForm()
        form.register("TestUser", "Test", "Test")
        db = dbClass.get_db()
        assert db.execute("SELECT username from user").fetchone()['username'] == "TestUser"
        assert db.execute("SELECT password from user where username = 'TestUser'").fetchone()['password'] == "Test"
        assert not (db.execute("SELECT password from user where username = 'TestUser'").fetchone()['password'] == "test")
        assert not (form.register("TestUser43", "Test", "test"))


def test_validate_password():
    assert register.RegistrationForm.validate_pass(register.RegistrationForm, "Test", "Test")
    assert not (register.RegistrationForm.validate_pass(register.RegistrationForm, "Test", "test"))

def test_validate_username():
    assert register.RegistrationForm.validate_user(register.RegistrationForm, "Test")
    assert not (register.RegistrationForm.validate_user(register.RegistrationForm, ""))
