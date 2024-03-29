from flask_wtf import FlaskForm
from wtforms import BooleanField, SubmitField, FileField, IntegerField, DateField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo

from DataGeneration import DataGeneration
from DataUpload import DataUpload

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

    def get_time_series_data(self):
        if self.file.filename != '':
            try:
                data_gen = DataUpload(self.file)
                date_series, value_series = data_gen.get_time_series()

            except Exception as e:
                flash(f"Error while generating data: {e}")
        
        else:
            # Initialize DataGeneration with form data
            try:
                data_gen = DataGeneration(self.channel_id.data, self.time_increment.data, self.field_id.data, self.start_date.data)
                date_series, value_series = data_gen.get_time_series()

            except Exception as e:
                flash(f"Error while generating data: {e}")  # Use flash for error messages