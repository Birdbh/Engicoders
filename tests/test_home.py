from flask import request
import sys
sys.path.append("src")
import flaskr.home as home
from werkzeug.datastructures import FileStorage
from sensors.sensor import Sensor

file_path = 'src/UPLOADED_DATA/data.xlsx'
with open(file_path, 'rb') as file:
        file_storage = FileStorage(stream=file, filename='data.xlsx', content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

sensor = Sensor("test", "test", [1, 2, 3], [1, 2, 3])

form_alarm ={
        'alarm_min': 500,
        'alarm_max': 50,
        'highlow': 1,
}

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

form_data_file_with_modifiers = {
            'channel_id': None,
            'field_id': None,
            'start_date': '2023-05-22 00:00:00',
            'time_increment': 15,
            'cleanse': False,
            'predict': True,
            'prediction_date': '2023-06-01',
            'chartType': 'line',  # Assuming this is a valid choice
            'stdDeviation': 2,
            'file': file_storage,
        }

form_data_file_without_modifiers = {
            'channel_id': None,
            'field_id': None,
            'start_date': None,
            'time_increment': 15,
            'cleanse': False,
            'predict': False,
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

def test_file_upload_and_modifier_validation():
      
      form = home.HomeForm(data=form_data_file_with_modifiers)
      assert(form.conflicting_modifers() == True)

def test_alarm_form():
        alarm_form = home.AlarmForm(data=form_alarm)

        assert alarm_form.alarm_min.data == 500

def test_apply_data_modifiers():
        form = home.HomeForm(data=form_data_file_without_modifiers)
        sensor_dummy = form.apply_data_modifiers(sensor)
        assert sensor_dummy.get_value() == [1, 2, 3]
        assert sensor_dummy.get_date_range() == [1, 2, 3]