from werkzeug.datastructures import FileStorage
import pandas as pd
import pytest
from unittest.mock import patch, MagicMock,mock_open
from io import BytesIO

import sys
sys.path.append("src")

from DataUpload import DataUpload

@pytest.fixture
def mock_file_storage():
    # Simulate file content with BytesIO
    file_content = b'Excel file content here'
    file_storage = MagicMock()
    file_storage.filename = 'data.xlsx'
    file_storage.stream = BytesIO(file_content)
    return file_storage

def test_object_creation(mock_file_storage):
    with patch('pandas.read_excel', return_value=pd.DataFrame()), \
         patch('DataUpload.os.makedirs'), patch("builtins.open", mock_open(read_data="data")):
        data_object = DataUpload(mock_file_storage)
        assert data_object is not None

def test_excel_to_dataframe(mock_file_storage):
    with patch('pandas.read_excel', return_value=pd.DataFrame()) as mock_read_excel:
        data_object = DataUpload(mock_file_storage)
        # No need to assert on pd.DataFrame() type directly; checking for DataFrame instance is enough
        assert isinstance(data_object.data_frame, pd.DataFrame)

def test_get_time_series(mock_file_storage):
    mock_df = pd.DataFrame({
        'Date': pd.date_range(start='2020-01-01', periods=3),
        'Value': [1, 2, 3]
    })
    with patch.object(DataUpload, 'read_excel_file', return_value=mock_df):
        data_object = DataUpload(mock_file_storage)
        date_range, value_range = data_object.get_time_series()
        assert date_range is not None and value_range is not None
        assert len(date_range) == len(value_range) == 3


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