import sys 
sys.path.append("src")

from sensors import sensor, Prediction, Cleanser

from datetime import datetime

mock_sensor = sensor.Sensor("Temperature Sensor", "Measures temperature", [datetime(2023, 1, 1), datetime(2023, 1, 2), datetime(2023, 1, 3), datetime(2023, 1, 4)], [22, 23, None, "23"])

sensor_with_cleansing = Cleanser.cleanser(mock_sensor, deviations=2)

sensor_with_cleansing_and_prediction = Prediction.DataPrediction(sensor_with_cleansing, datetime(2023, 1, 7))

def test_process_sensor_data():
    print(mock_sensor.process_data())
    assert mock_sensor.process_data() == ([datetime(2023, 1, 1, 0, 0), datetime(2023, 1, 2, 0, 0), datetime(2023, 1, 3, 0, 0), datetime(2023, 1, 4, 0, 0)], [22, 23, None, "23"])

def test_sensor_with_cleansing():
    assert sensor_with_cleansing.process_data() == ([datetime(2023, 1, 1, 0, 0), datetime(2023, 1, 2, 0, 0), datetime(2023, 1, 3, 0, 0), datetime(2023, 1, 4, 0, 0)], [22.0, 23.0, 23.0, 23.0])

def test_sensor_with_cleansing_and_prediction():
    assert sensor_with_cleansing_and_prediction.process_data() == ([datetime(2023, 1, 1, 0, 0), datetime(2023, 1, 2, 0, 0), datetime(2023, 1, 3, 0, 0), datetime(2023, 1, 4, 0, 0)], [22.0, 23.0, 23.0, 23.0], [datetime(2023, 1, 5, 0, 0), datetime(2023, 1, 6, 0, 0), datetime(2023, 1, 7, 0, 0)], [0.0, 0.0, 0.0])
