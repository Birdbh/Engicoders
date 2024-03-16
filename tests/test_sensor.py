import pytest

import sys
sys.path.append("src")

from sensors.sensor import Sensor
import datetime as dt



def test_create_sensor():
    sensor = Sensor("Temperature Sensor", "Measures Temperature", [dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 3)], [1, 2, 3])
    assert sensor.name == "Temperature Sensor"
    assert sensor.description == "Measures Temperature"
    assert sensor.value == [1,2,3]
    assert str(sensor) == "NAME:Temperature Sensor, DESCRIPTION:Measures Temperature, DATE-RANGE:[datetime.datetime(2020, 1, 1, 0, 0), datetime.datetime(2020, 1, 2, 0, 0), datetime.datetime(2020, 1, 3, 0, 0)], VALUES:[1, 2, 3]"

def test_update_sensor():
    sensor = Sensor("Temperature Sensor", "Measures Temperature", [dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 3)], [1, 2, 3])
    sensor.set_name("Humidity Sensor")
    sensor.set_description("Measures Humidity")

    with pytest.raises(Exception) as e:
        sensor.set_value([50])

    assert str(e.value) == "The length of the new value must be equal to the length of the date range"

    assert sensor.name == "Humidity Sensor"
    assert sensor.description == "Measures Humidity"
    assert sensor.value == [1,2,3]
    assert str(sensor) == "NAME:Humidity Sensor, DESCRIPTION:Measures Humidity, DATE-RANGE:[datetime.datetime(2020, 1, 1, 0, 0), datetime.datetime(2020, 1, 2, 0, 0), datetime.datetime(2020, 1, 3, 0, 0)], VALUES:[1, 2, 3]"

def test_forecast_sensor():
    sensor = Sensor("Temperature Sensor", "Measures Temperature", [dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 3)], [1, 2, 3])
    sensor.set_forecast_values([2,4,6])
    sensor.set_forecast_date_range([dt.datetime(2020, 1, 4), dt.datetime(2020, 1, 5), dt.datetime(2020, 1, 6)])
    assert sensor.get_forecast_values() == [2,4,6]
    assert sensor.get_forecast_date_range() == [dt.datetime(2020, 1, 4), dt.datetime(2020, 1, 5), dt.datetime(2020, 1, 6)]