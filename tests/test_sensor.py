import pytest

import sys
sys.path.append("src")

from sensors.sensor import Sensor

def test_create_sensor():
    sensor = Sensor(1, "Temperature Sensor", "Measures Temperature", "Temperature", { "1": 1, "2": 2, "3" : 3},)
    print(sensor.value)
    assert sensor.id == 1
    assert sensor.name == "Temperature Sensor"
    assert sensor.description == "Measures Temperature"
    assert sensor.type == "Temperature"
    assert sensor.value == {'1': 1, '2': 2, '3': 3}
    assert str(sensor) == "Sensor: ID:1, NAME:Temperature Sensor, DESCRIPTION:Measures Temperature, DATA-TYPE:Temperature, VALUES: {'1': 1, '2': 2, '3': 3}"

def test_update_sensor():
    sensor = Sensor(1, "Temperature Sensor", "Measures Temperature", "Temperature", 72)
    sensor.set_name("Humidity Sensor")
    sensor.set_description("Measures Humidity")
    sensor.set_type("Humidity")
    sensor.set_value(50)
    assert sensor.id == 1
    assert sensor.name == "Humidity Sensor"
    assert sensor.description == "Measures Humidity"
    assert sensor.type == "Humidity"
    assert sensor.value == 50
    assert str(sensor) == "Sensor: ID:1, NAME:Humidity Sensor, DESCRIPTION:Measures Humidity, DATA-TYPE:Humidity, VALUES: 50"

def test_forecast_sensor():
    sensor = Sensor(1, "Temperature Sensor", "Measures Temperature", "Temperature", 72)
    sensor.set_forecast_values({ "1": 73, "2": 74, "3" : 75})
    assert sensor.get_forecast_values() == { "1": 73, "2": 74, "3" : 75}
    assert sensor.get_forecast_values()["1"] == 73
    assert sensor.get_forecast_values()["2"] == 74
    assert sensor.get_forecast_values()["3"] == 75