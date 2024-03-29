from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, FileField, IntegerField, DateField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from flask import Flask, render_template, flash
from flaskr.db import get_db
from flaskr.user import User
from flask_login import login_user

class HomeForm(FlaskForm):
    channel_id = IntegerField('Channel ID', validators=[DataRequired()])
    field_id = IntegerField('Field ID', validators=[DataRequired()])
    start_date = DateField('Start Date', validators=[DataRequired()])
    time_increment = IntegerField('Time Increment', validators=[DataRequired()])  # Modify choices as needed
    cleanse = BooleanField('Cleanse Data')
    predict = BooleanField('Predict Data')
    prediction_date = DateField('Prediction Date')
    chartType = SelectField('Chart Type', choices=[('line', 'bar', 'radio')])  # Modify choices as needed
    stdDeviation = IntegerField('Standard Deviation')
    file = FileField('File Upload')
    submit = SubmitField('Submit')