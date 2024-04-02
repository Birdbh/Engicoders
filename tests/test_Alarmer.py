import sys
sys.path.append("src")
from sensors.sensor import Sensor
import datetime as dt 
from Alarmer import Alarmer

sensor1 = Sensor("Temperature Sensor", "Measures Temperature", [dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 3), dt.datetime(2020, 1, 4)], [1,2, 3, 10])

highThreshold = 10
lowThreshold = 3


def test_create_Alarmer_and_makes_a_list_of_high_and_low_thresholds():
    alarmer = Alarmer(sensor1, highThreshold, lowThreshold)
    assert alarmer.sensor == sensor1
    assert alarmer.highThreshold == 10
    assert alarmer.lowThreshold == 3
    assert alarmer.get_high_threshold() == [10,10,10,10]
    assert alarmer.get_low_threshold() == [3,3,3,3]