import pytest

import sys
sys.path.append("src")
from sensors.sensor import Sensor
from sensors.Cleanser import cleanser
import datetime as dt  


sensor1 = Sensor("Temperature Sensor", "Measures Temperature", [dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 3), dt.datetime(2020, 1, 4)], [1,2, 3, 10])
sensor2 = Sensor("Temperature Sensor", "Measures Temperature", [dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 3), dt.datetime(2020, 1, 4), dt.datetime(2020, 1, 5), dt.datetime(2020, 1, 6), dt.datetime(2020, 1, 7)], [1,2, 3, 20, 1, 2, 2])
sensor3 = Sensor("Temperature Sensor", "Measures Temperature", [dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 3), dt.datetime(2020, 1, 4)], [50,55,2,60])
sensor4 = Sensor("Temperature Sensor", "Measures Temperature", [dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 3), dt.datetime(2020, 1, 4), dt.datetime(2020, 1, 5)], [50,55,2,60, 100])

#This is what a sensor should look like in the updated format
sensor7 = Sensor("Temperature Sensor", "Measures Temperature", [dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 3)], [None, 3, None])

sensor8 = Sensor("Temperature Sensor", "Measures Temperature", [dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 3)], ["47", 3, "1"])


def test_create_cleanser():
    cleaner = cleanser(sensor1, 1)
    assert cleaner.sensor == sensor1
    assert cleaner.deviations == 1

def test_get_mean():
    cleaner = cleanser(sensor1, 1)
    assert cleaner.get_mean() == 4

def test_get_standard_deviation():
    cleaner = cleanser(sensor1, 1)
    assert cleaner.get_standard_dev() == (50/3)**0.5

def test_remove_outliers():
    cleaner = cleanser(sensor1, 1)
    assert cleaner.remove_outlier() == [1,2,3]

def test_remove_outliers_higher_deviation_count():
    cleaner = cleanser(sensor2, 2)
    assert cleaner.remove_outlier() == [1,2,3,1,2,2]

def test_remove_outliers_low_outlier():
    cleaner = cleanser(sensor3, 1)
    assert cleaner.remove_outlier() == [50,55,60]

def test_remove_low_and_high_outlier():
    cleaner = cleanser(sensor4, 1)
    assert cleaner.remove_outlier() == [50,55,60]

def test_replace_missing_values():
    cleaner = cleanser(sensor7, 1)
    assert cleaner.replace_missing_values() == [0, 3, 3]

def test_set_data_types_to_float():
    cleaner = cleanser(sensor8, 1)
    assert cleaner.set_data_types_to_float() == [47, 3, 1]
