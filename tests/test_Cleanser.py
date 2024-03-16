import pytest

import sys
sys.path.append("src")
from sensors.sensor import Sensor
from sensors.Cleanser import cleanser
import datetime as dt  


sensor = Sensor(1, "Temperature Sensor", "Measures Temperature", "Temperature", { "1": 1, "2": 2, "3" : 3, "4": 10},)
sensor2 =Sensor(1, "Temperature Sensor", "Measures Temperature", "Temperature", { "1": 1, "2": 2, "3" : 3, "4": 20, "5": 1, "6": 2, "7": 2},)
sensor3 =Sensor(1, "Temperature Sensor", "Measures Temperature", "Temperature", { "1": 50, "2": 55, "3" : 2, "4": 60},)
sensor4 =Sensor(1, "Temperature Sensor", "Measures Temperature", "Temperature", { "1": 50, "2": 55, "3" : 2, "4": 60, "5":100},)
sensor5 =Sensor(1, "Temperature Sensor", "Measures Temperature", "Temperature", { "1": None, "2": 2, "3" : None, "4": 10},)
sensor6 = Sensor(1, "Temperature Sensor", "Measures Temperature", "Temperature", { "1": "1", "2": "2", "3" : "3", "4": "10"},)

#This is what a sensor should look like in the updated format
sensor7 = Sensor("Temperature Sensor", "Measures Temperature", [dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 3)], [None, 3, None])

sensor8 = Sensor("Temperature Sensor", "Measures Temperature", [dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 3)], ["47", 3, "1"])


def test_create_cleanser():
    cleaner = cleanser(sensor, 1)
    assert cleaner.sensor == sensor
    assert cleaner.deviations == 1

def test_get_mean():
    cleaner = cleanser(sensor, 1)
    assert cleaner.get_mean() == 4

def test_get_standard_deviation():
    cleaner = cleanser(sensor, 1)
    assert cleaner.get_standard_dev() == (50/3)**0.5

def test_remove_outliers():
    cleaner = cleanser(sensor, 1)
    assert cleaner.remove_outlier() == {"1": 1, "2": 2, "3": 3}

def test_remove_outliers_higher_deviation_count():
    cleaner = cleanser(sensor2, 2)
    assert cleaner.remove_outlier() == { "1": 1, "2": 2, "3" : 3, "5": 1, "6": 2, "7": 2}

def test_remove_outliers_low_outlier():
    cleaner = cleanser(sensor3, 1)
    assert cleaner.remove_outlier() == { "1": 50, "2": 55, "4": 60}

def test_remove_low_and_high_outlier():
    cleaner = cleanser(sensor4, 1)
    assert cleaner.remove_outlier() == { "1": 50, "2": 55, "4": 60}

def test_replace_missing_values():
    cleaner = cleanser(sensor7, 1)
    assert cleaner.replace_missing_values() == [0, 3, 3]

def test_set_data_types_to_float():
    cleaner = cleanser(sensor8, 1)
    assert cleaner.set_data_types_to_float() == [47, 3, 1]
