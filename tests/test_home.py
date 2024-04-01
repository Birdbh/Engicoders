import pytest
from flask import Flask, request

import pytest
import sys
from flask_wtf import FlaskForm

from flask import Flask, render_template
sys.path.append("src")

import flaskr.home as home

import flaskr.db as dbClass

from werkzeug.datastructures import FileStorage

file_path = 'src/UPLOADED_DATA/data.xlsx'
with open(file_path, 'rb') as file:
        file_storage = FileStorage(stream=file, filename='data.xlsx', content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

form_data_None = {
            'channel_id': None,
            'field_id': None,
            'start_date': None,
            'time_increment': None,
            'cleanse': None,
            'predict': None,
            'prediction_date': None,
            'chartType': None,  # Assuming this is a valid choice
            'stdDeviation': None,
            'file': None,
        }

form_data_duplicate = {
            'channel_id': 1,
            'field_id': 1,
            'start_date': '2023-01-01',
            'time_increment': 15,
            'cleanse': True,
            'predict': True,
            'prediction_date': '2023-06-01',
            'chartType': 'line',  # Assuming this is a valid choice
            'stdDeviation': 2,
            'file': file_storage,
        }

form_data_file = {
            'channel_id': None,
            'field_id': None,
            'start_date': None,
            'time_increment': 15,
            'cleanse': True,
            'predict': True,
            'prediction_date': '2023-06-01',
            'chartType': 'line',  # Assuming this is a valid choice
            'stdDeviation': 2,
            'file': file_storage,
        }

def test_home(app):
    with app.test_request_context():
        form = home.HomeForm()
        assert form.conflicting_input()

def test_file_upload_and_validation():

        # Instantiate the form with the simulated file and data
        form = home.HomeForm(data=form_data_file)

        # Check for conflicting input where there should be none
        assert(form.conflicting_input() == False)

        form = home.HomeForm(data=form_data_duplicate)

        # Check for conflicting input where there should be
        assert(form.conflicting_input() == True)

        form = home.HomeForm(data=form_data_None)

         # Check for conflicting input where there should be
        assert(form.conflicting_input() == True)