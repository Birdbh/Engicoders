import pytest
from src.sensors.sensor import Sensor

def test_sensor():
    sensor = Sensor(1, "Temperature Sensor", "Measures Temperature", "Temperature", { "1": 1, "2": 2, "3" : 3},)
    print(sensor.value)
    assert sensor.id == 1
    assert sensor.name == "Temperature Sensor"
    assert sensor.description == "Measures Temperature"
    assert sensor.type == "Temperature"
    assert sensor.value == 72
    assert str(sensor) == "Sensor: ID:1, NAME:Temperature Sensor, DESCRIPTION:Measures Temperature, DATA-TYPE:Temperature, VALUES: 72"

test_sensor()