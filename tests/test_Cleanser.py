import sys
sys.path.append("src")
from sensors.sensor import Sensor
from sensors.Cleanser import cleanser
import datetime as dt  
import pytest

sensor1 = Sensor("Temperature Sensor", "Measures Temperature", [dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 3), dt.datetime(2020, 1, 4)], [1,2, 3, 10])
sensor2 = Sensor("Temperature Sensor", "Measures Temperature", [dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 3), dt.datetime(2020, 1, 4), dt.datetime(2020, 1, 5), dt.datetime(2020, 1, 6), dt.datetime(2020, 1, 7)], [1,2, 3, 20, 1, 2, 2])
sensor4 = Sensor("Temperature Sensor", "Measures Temperature", [dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 3), dt.datetime(2020, 1, 4), dt.datetime(2020, 1, 5)], [2,50,55,60, 100])
sensor5 = Sensor("Temperature Sensor", "Measures Temperature", [dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 3), dt.datetime(2020, 1, 4), dt.datetime(2020, 1, 5)], [2,100,55,60, 100])
#This is what a sensor should look like in the updated format
sensor7 = Sensor("Temperature Sensor", "Measures Temperature", [dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 3)], [None, 3, None])

sensor8 = Sensor("Temperature Sensor", "Measures Temperature", [dt.datetime(2020, 1, 1), dt.datetime(2020, 1, 2), dt.datetime(2020, 1, 3)], ["47", 3, "1"])


def test_create_cleanser_check_mean_and_sdev():
    cleaner = cleanser(sensor1, 1)
    assert cleaner.sensor == sensor1
    assert cleaner.deviations == 1
    assert cleaner.get_mean() == 4
    assert cleaner.get_standard_dev() == (50/3)**0.5

def test_remove_outliers_higher_deviation_count():
    cleaner = cleanser(sensor2, 2)
    assert cleaner.remove_outlier() == [1,2,3,3,1,2,2]

def test_remove_low_and_high_outlier_one_at_edge():
    cleaner = cleanser(sensor4, 1)
    assert cleaner.remove_outlier() == [0,50,55,60,60]

def test_remove_max_and_min_one_at_start_and_multiple_max():
    cleaner = cleanser(sensor5, 1)
    assert cleaner.remove_max() == [2,2,55,60,60]
    assert cleaner.remove_min() == [0,0,55,60,60]

def test_handle_empty_data():
    empty_sensor = Sensor("Empty Sensor", "Test Sensor with no data", [], [])
    cleaner = cleanser(empty_sensor, 1)
    assert cleaner.get_mean() == 0
    assert cleaner.get_standard_dev() == 0
    assert cleaner.remove_outlier() == []

def test_extreme_deviation_values():
    normal_sensor = Sensor("Normal Sensor", "Sensor with normal range data",
                           [dt.datetime(2020, 1, 1)], [1, 2, 3, 4, 5])
    cleaner_high_dev = cleanser(normal_sensor, 1000)  # Extremely high deviation
    cleaner_low_dev = cleanser(normal_sensor, 0)  # Extremely low deviation
    assert cleaner_high_dev.remove_outlier() == [1, 2, 3, 4, 5]
    assert cleaner_low_dev.remove_outlier() == [0, 0, 3, 3, 3]


def test_replace_missing_values():
    cleaner = cleanser(sensor7, 1)
    assert cleaner.replace_missing_values() == [0, 3, 3]

def test_set_data_types_to_float():
    cleaner = cleanser(sensor8, 1)
    assert cleaner.set_data_types_to_float() == [47, 3, 1]
