import pandas as pd
from typing import Tuple, List
import os

NAME_OF_DATA_FILE = "data.xlsx"
LOCATION_OF_DATA_FILE = "UPLOADED_DATA/" +NAME_OF_DATA_FILE

directory = os.path.dirname(LOCATION_OF_DATA_FILE)
if not os.path.exists(directory):
    os.makedirs(directory)

class DataUpload:
    def __init__(self, file):
        self.file = file
        self.file.filename = NAME_OF_DATA_FILE
        self.file.save(LOCATION_OF_DATA_FILE)
        self.data_frame = self.read_excel_file(LOCATION_OF_DATA_FILE)

    def read_excel_file(self, file_path: str) -> pd.DataFrame:
        """
        Reads an Excel file and returns its content as a pandas DataFrame.
        """
        return pd.read_excel(file_path)

    def parse_datetime_column(self, data_frame: pd.DataFrame) -> List:
        """
        Parses the first column of the DataFrame to datetime objects and returns them as a list.
        """
        return pd.to_datetime(self.data_frame.iloc[:, 0]).dt.to_pydatetime().tolist()

    def parse_integer_column(self, data_frame: pd.DataFrame) -> List:
        """
        Parses the second column of the DataFrame to a list of integers.
        """
        return data_frame.iloc[:, 1].astype(int).tolist()

    def get_time_series(self) -> Tuple[List, List]:
        """
        Processes the Excel file and returns the dates and values as lists.
        """
        date_range = self.parse_datetime_column(self.data_frame)
        value_range = self.parse_integer_column(self.data_frame)
        return date_range, value_range
    