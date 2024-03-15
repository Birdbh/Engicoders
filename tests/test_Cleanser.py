import pytest

import sys
sys.path.append("src")
from sensors.sensor import Sensor
from sensors.Cleanser import cleanser
import sensors.Cleanser

sensor = Sensor(1, "Temperature Sensor", "Measures Temperature", "Temperature", { "1": 1, "2": 2, "3" : 3, "4": 10},)
sensor2 =Sensor(1, "Temperature Sensor", "Measures Temperature", "Temperature", { "1": 1, "2": 2, "3" : 3, "4": 20, "5": 1, "6": 2, "7": 2},)
sensor3 =Sensor(1, "Temperature Sensor", "Measures Temperature", "Temperature", { "1": 50, "2": 55, "3" : 2, "4": 60},)
sensor4 =Sensor(1, "Temperature Sensor", "Measures Temperature", "Temperature", { "1": 50, "2": 55, "3" : 2, "4": 60, "5":100},)
sensor5 =Sensor(1, "Temperature Sensor", "Measures Temperature", "Temperature", { "1": None, "2": 2, "3" : None, "4": 10},)
sensor6 = Sensor(1, "Temperature Sensor", "Measures Temperature", "Temperature", { "1": "1", "2": "2", "3" : "3", "4": "10"},)



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
    cleaner = cleanser(sensor5, 1)
    assert cleaner.replace_missing_values() == [0, 2, 2, 10]

def test_set_data_types_to_float():
    cleaner = cleanser(sensor6, 1)
    assert cleaner.set_data_types_to_float() == [1, 2, 3, 10]
