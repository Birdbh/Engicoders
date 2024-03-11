import pytest

import sys
sys.path.append("src")
from sensors.sensor import Sensor
from sensors.Cleanser import cleanser
import sensors.Cleanser

sensor = Sensor(1, "Temperature Sensor", "Measures Temperature", "Temperature", { "1": 1, "2": 2, "3" : 3, "4": 10},)

def test_create_cleanser():
    cleaner = cleanser(sensor, 1)
    assert cleaner.sensor == sensor
    assert cleaner.deviations == 2

def test_get_mean():
    cleaner = cleanser(sensor, 1)
    assert cleaner.get_mean() == 4

def test_get_standard_deviation():
    cleaner = cleanser(sensor, 1)
    assert cleaner.get_standard_dev() == (50/3)**0.5

def test_remove_outliers():
    cleaner = cleanser(sensor, 1)
    assert cleaner.remove_outlier() == {"1": 1, "2": 2, "3": 3}

