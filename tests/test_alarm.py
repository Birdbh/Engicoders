import pytest
from unittest.mock import MagicMock, patch
import socketio.exceptions
from sensors.alarm import Alarm

@pytest.fixture
def mock_sensor():
    sensor = MagicMock()
    sensor.get_name.return_value = "Mock Sensor"
    sensor.get_value.return_value = 0
    return sensor

# Fixture for the alarm to include setup with mock_socketio
@pytest.fixture
@patch('sensors.alarm.socketio.Client')
def alarm(mock_socketio, mock_sensor):
    alarm = Alarm(mock_sensor, 10, "High")
    return alarm

# Test initialization and successful connection
def test_alarm_initialization(alarm):
    assert alarm.sensor.get_name() == "Mock Sensor"
    assert alarm.threshold == 10
    assert alarm.importance == "High"
    assert not alarm.is_set
    alarm.sio.connect.assert_called_with('http://127.0.0.1:5000/')

# Test the set_alarm method
def test_set_alarm(alarm):
    assert not alarm.is_set
    alarm.set_alarm()
    assert alarm.is_set

# Test the check_sensor method without triggering the alarm
def test_check_sensor_no_alert(alarm, mock_sensor):
    alarm.set_alarm()
    alarm.check_sensor()
    alarm.sio.emit.assert_not_called()

# Test the delete_alarm method
def test_delete_alarm(alarm):
    alarm.set_alarm()
    assert alarm.is_set
    alarm.delete_alarm()
    assert not alarm.is_set

# Test the change_threshold method
def test_change_threshold(alarm):
    assert alarm.threshold == 10
    new_threshold = 20
    alarm.change_threshold(new_threshold)
    assert alarm.threshold == new_threshold

# Test alert_alarm_with_socket_io_emit
def test_alert_alarm_with_socket_io_emit(alarm, mock_sensor):
    mock_sensor.get_value.return_value = 15
    alarm.set_alarm()
    alarm.check_sensor()
    # Verify Socket.IO emit was called with correct parameters
    alarm.sio.emit.assert_called_with('alarm_message', {'message': 'Alarm! Mock Sensor has exceeded the threshold with a value of 15.'})

# Test Alarm initialization failure due to Socket.IO connection error
@patch('sensors.alarm.socketio.Client')
def test_alarm_initialization_failure(mock_socketio, mock_sensor):
    mock_socketio.return_value.connect.side_effect = socketio.exceptions.ConnectionError("Test Connection Error")
    with patch('logging.error') as mock_logging_error:
        Alarm(mock_sensor, 10, "High")
        mock_logging_error.assert_called()

# Test for Sensor Value Exactly at Threshold
def test_check_sensor_at_threshold(alarm, mock_sensor):
    mock_sensor.get_value.return_value = 10
    alarm.set_alarm()
    alarm.check_sensor()
    # Depending on the implementation, adjust the assertion
    alarm.sio.emit.assert_not_called()

# Directly Test log_message Method
@patch('sensors.alarm.logging.info')
def test_log_message(mock_logging_info, alarm):
    message = "Testing log message."
    alarm.log_message(message)
    mock_logging_info.assert_called_with(message)

# Test disconnect method
def test_disconnect(alarm):
    alarm.disconnect()
    alarm.sio.disconnect.assert_called()
