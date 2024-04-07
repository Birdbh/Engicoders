from werkzeug.datastructures import FileStorage
import pandas as pd

import sys
sys.path.append("src")

from DataUpload import DataUpload

def test_objection_creation_and_execution():

    file_path = 'src/UPLOADED_DATA/data.xlsx'
    with open(file_path, 'rb') as file:
        file_storage = FileStorage(stream=file, filename='data.xlsx', content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        data_object = DataUpload(file_storage)

    #confirm object is created
    assert data_object is not None

    #excel file is made to dataframe
    assert type(data_object.read_excel_file(file_path)) == type(pd.DataFrame())

    #data is returned from dataframe
    assert data_object.get_time_series() is not None