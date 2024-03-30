from werkzeug.datastructures import FileStorage

import sys
sys.path.append("src")

from DataUpload import DataUpload  # Import your actual module here

# Path to the Excel file you want to upload (adjust as necessary)
file_path = 'src/UPLOADED_DATA/data.xlsx'

# Create a FileStorage instance to simulate the file being uploaded
with open(file_path, 'rb') as file:
    file_storage = FileStorage(stream=file, filename='data.xlsx', content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

# Instantiate DataUpload with the mocked file
data_upload_instance = DataUpload(file_storage)

# Now you can call methods on your data_upload_instance as needed for testing
date_series, value_series = data_upload_instance.get_time_series()
