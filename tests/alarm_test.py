import pytest
from unittest.mock import MagicMock, patch
import sys
sys.path.append("src")
from sensors.alarm import Alarm

@pytest.fixture
def mock_sensor():
    sensor = MagicMock()
    sensor.get_name.return_value = "Mock Sensor"
    sensor.get_value.return_value = 0
    return sensor

# Adjusted the patch path to reflect actual module structure
@pytest.fixture
@patch('sensors.alarm.socketio.Client')
def alarm(mock_socketio, mock_sensor):
    alarm = Alarm(mock_sensor, 10, "High")
    return alarm

def test_set_alarm(alarm, mock_sensor):
    assert not alarm.is_set
    alarm.set_alarm()
    assert alarm.is_set

def test_alert_alarm_with_socket_io_emit(alarm, mock_sensor):
    mock_sensor.get_value.return_value = 15
    alarm.set_alarm()
    alarm.check_sensor()
    # Verify Socket.IO emit was called with correct parameters
    alarm.sio.emit.assert_called_with('alarm_message', {'message': 'Alarm! Mock Sensor has exceeded the threshold with a value of 15.'})
