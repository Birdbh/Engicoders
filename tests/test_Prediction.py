import pytest
import datetime as dt

import sys
sys.path.append("src")

from Prediction import DataPrediction
from sensors.sensor import Sensor

sensor = Sensor("Temperature Sensor", "Measures Temperature", [dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 3)], [47, 3, 1])

def test___init__():
    end_date = dt.datetime(2020, 1, 6)
    dp = DataPrediction(sensor, end_date)
    assert dp.X == sensor.get_date_range()
    assert dp.prediction_intervals == dt.timedelta(days=1)
    assert dp.prediction_start_date == dt.datetime(2020, 1, 4)
    assert dp.prediction_end_date == end_date

def test_set_prediction_timeframe():
    dp = DataPrediction(sensor, dt.datetime(2020, 1, 6))
    dp.set_prediction_timeframe()
    assert dp.X_future == [dt.datetime(2020, 1, 4), dt.datetime(2020, 1, 5), dt.datetime(2020, 1, 6)]

def test_train_model():
    dp = DataPrediction(sensor, dt.datetime(2020, 1, 6))
    dp.train_model()
    assert dp.model is not None

def test_predict():
    dp = DataPrediction(sensor, dt.datetime(2020, 1, 6))
    dp.set_prediction_timeframe()
    dp.train_model()
    dp.predict()
    assert dp.forcasted_values == [0.0, 0.0, 0.0]