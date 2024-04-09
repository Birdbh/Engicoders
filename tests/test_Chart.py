import sys
sys.path.append("src")
from sensors.sensor import Sensor
import datetime as dt 
from Chart import Chart
import pytest

sensor1 = Sensor("Temperature Sensor", "Measures Temperature", [dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 3), dt.datetime(2020, 1, 4)], [1,2, 3, 10])


@pytest.fixture
def sensor_instance():
    return Sensor("Temperature Sensor", "Measures Temperature", 
                  [dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 3), dt.datetime(2020, 1, 4)], 
                  [1, 2, 3, 10])

# Test class for Chart
class TestChart:
    # Use the sensor_instance fixture to provide a Sensor object to each test method
    def test_chart_initialization(self, sensor_instance):
        chart = Chart(sensor_instance)
        assert chart.sensor == sensor_instance, "Chart sensor attribute should match the provided Sensor instance"

    def test_get_values(self, sensor_instance):
        chart = Chart(sensor_instance)
        expected_values = ["1", "2", "3", "10"]
        assert chart.get_values() == expected_values, "get_values should return a list of string representations of the sensor values"

    def test_get_labels(self, sensor_instance):
        chart = Chart(sensor_instance)
        expected_labels = ["2020-01-01 00:00:00", "2020-01-02 00:00:00", "2020-01-03 00:00:00", "2020-01-04 00:00:00"]
        assert chart.get_labels() == expected_labels