from werkzeug.datastructures import FileStorage

import sys
sys.path.append("src")
import flaskr.home as home

from DataUpload import DataUpload  # Import your actual module here

# Path to the Excel file you want to upload (adjust as necessary)
file_path = 'src/UPLOADED_DATA/data.xlsx'

# Create a FileStorage instance to simulate the file being uploaded
# with open(file_path, 'rb') as file:
#     file_storage = FileStorage(stream=file, filename='data.xlsx', content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

# # Instantiate DataUpload with the mocked file
# data_upload_instance = DataUpload(file_storage)
from conftest import app

# Now you can call methods on your data_upload_instance as needed for testing
# date_series, value_series = data_upload_instance.get_time_series()

import os
from werkzeug.datastructures import FileStorage

def test_file_upload(app):
    # Path to the mock Excel file you want to upload
    file_path = 'path/to/mock/data.xlsx'
    with app.test_client() as client:
        with open(file_path, 'rb') as file:
            data = {
                # Include other form fields as necessary
                'file': (file, 'data.xlsx'),
            }
            response = client.post('/your-endpoint', data=data, content_type='multipart/form-data')
            
            # Perform your assertions here
            assert response.status_code == 200
            # Add more assertions based on what you expect to happen

from flask import request, flash

@app.route('/home', methods=['POST'])
def handle_form_submission():
    form = home.HomeForm(request.form)
    if form.validate_on_submit():
        if 'file' in request.files:
            file = request.files['file']
            if file:
                try:
                    data_upload_instance = DataUpload(file)
                    date_series, value_series = data_upload_instance.get_time_series()
                    # Handle the success case, maybe return a success response or render a template
                except Exception as e:
                    flash(f"Error processing file: {e}")
                    # Handle the error case
    # Ensure to return a response or render a template even in case of failure

test_file_upload()