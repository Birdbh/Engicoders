import pytest
from flask import Flask, request
from flaskr import create_app  # Adjust this import based on your project structure

import pytest
import sys
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from flask import Flask, render_template
sys.path.append("src")
import flaskr.home as home

import flaskr.db as dbClass


def test_home(app):
    with app.test_request_context():
        form = home.HomeForm()
        assert form.conflicting_input()
