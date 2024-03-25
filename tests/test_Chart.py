import sys
sys.path.append("src")
from sensors.sensor import Sensor
from sensors.Cleanser import cleanser
import datetime as dt 
from Chart import Chart 

sensor1 = Sensor("Temperature Sensor", "Measures Temperature", [dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 3), dt.datetime(2020, 1, 4)], [1,2, 3, 10])

def test_create_chart_instance():
    charter = Chart(sensor1)
    assert charter.sensor == sensor1
    assert charter.get_values() == [1,2, 3, 10]
    assert charter.get_labels() == ["2020-01-01 00:00:00","2020-01-02 00:00:00","2020-01-03 00:00:00","2020-01-04 00:00:00"]
