import pytest
from unittest.mock import MagicMock
import sys
sys.path.append("src")
from sensors.alarm import Alarm
import time

@pytest.fixture
def mock_sensor():
    sensor = MagicMock()
    sensor.get_name.return_value = "Mock Sensor"
    sensor.get_value.return_value = 0
    return sensor

@pytest.fixture
def mock_on_trigger():
    return MagicMock(name='on_trigger')

@pytest.fixture
def alarm(mock_sensor, mock_on_trigger):
    return Alarm(mock_sensor, threshold=10, deadband=1, delay=0, on_trigger=mock_on_trigger)

def test_set_alarm(alarm):
    assert not alarm.is_set
    alarm.set_alarm()
    assert alarm.is_set

def test_clear_alarm(alarm):
    alarm.set_alarm()
    alarm.clear_alarm()
    assert not alarm.is_set
    assert not alarm.is_alarm_active()

def test_check_sensor_without_trigger(alarm, mock_sensor):
    mock_sensor.get_value.return_value = 9  # Below the threshold
    alarm.set_alarm()
    alarm.check_sensor()
    assert not alarm.is_alarm_active()

def test_check_sensor_with_trigger(alarm, mock_sensor, mock_on_trigger):
    mock_sensor.get_value.return_value = 12  # Above the threshold
    alarm.set_alarm()
    alarm.check_sensor()
    mock_on_trigger.assert_called_once()

def test_sensor_value_within_deadband_does_not_trigger_alarm(alarm, mock_sensor, mock_on_trigger):
    mock_sensor.get_value.return_value = 10.5  # Assuming a threshold of 10 and a deadband of 1
    alarm.set_alarm()
    alarm.check_sensor()
    mock_on_trigger.assert_not_called()

def test_alarm_does_not_trigger_when_not_set(alarm, mock_sensor, mock_on_trigger):
    mock_sensor.get_value.return_value = 15  # Above the threshold
    alarm.check_sensor()
    mock_on_trigger.assert_not_called()

def test_updating_threshold_and_deadband(alarm, mock_sensor, mock_on_trigger):
    alarm.threshold = 15
    alarm.deadband = 2
    alarm.set_alarm()
    mock_sensor.get_value.return_value = 14
    alarm.check_sensor()
    mock_on_trigger.assert_not_called()  # Below the new threshold
    mock_sensor.get_value.return_value = 18
    alarm.check_sensor()
    mock_on_trigger.assert_called_once()  # Above the new threshold and outside deadband
