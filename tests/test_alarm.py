import pytest
from unittest.mock import MagicMock, patch
import sys
sys.path.append("src")
from sensors.alarm import Alarm
import time

# This fixture creates a mock Sensor object.
@pytest.fixture
def mock_sensor():
    sensor = MagicMock()
    sensor.get_name.return_value = "Mock Sensor"
    sensor.get_value.return_value = 0
    return sensor

# This fixture creates an Alarm object with the mock Sensor.
@pytest.fixture
def alarm(mock_sensor):
    # Create a mock for the on_trigger callback
    mock_on_trigger = MagicMock()
    alarm = Alarm(mock_sensor, threshold=10, deadband=1, delay=0, on_trigger=mock_on_trigger)
    return alarm

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
    # The alarm should be triggered immediately since there is no delay
    mock_on_trigger.assert_called_once()

def test_check_sensor_with_delay(alarm, mock_sensor, mock_on_trigger):
    mock_sensor.get_value.return_value = 12  # Above the threshold
    alarm.delay = 5  # Delay of 5 seconds for the sake of the test
    alarm.set_alarm()
    # Simulate time before the delay has passed
    with patch('sensors.alarm.time.time', return_value=time.time()):
        alarm.check_sensor()
        # Initially, the alarm should not be triggered because the delay has not passed
        assert not alarm.is_alarm_active()
        mock_on_trigger.assert_not_called()
    
    # Fast-forward time to simulate the delay passing
    with patch('sensors.alarm.time.time', return_value=time.time() + alarm.delay + 1):
        alarm.check_sensor()
        # Now the alarm should be triggered
        assert alarm.is_alarm_active()
        mock_on_trigger.assert_called_once()
