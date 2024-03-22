import pytest
from unittest.mock import MagicMock, patch, create_autospec
import sys
sys.path.append("src")
from sensors.alarm import Alarm
from alarmManager import AlarmManager


@pytest.fixture
def mock_sio_client():
    with patch('socketio.Client') as mock:
        yield mock

@pytest.fixture
def alarm_manager(mock_sio_client):
    return AlarmManager(server_address="http://127.0.0.1:5000/")

@pytest.fixture
def mock_alarm():
    alarm = Alarm(sensor=MagicMock(), threshold=10, deadband=1, delay=0, on_trigger=None)
    alarm.on_trigger = MagicMock()
    return alarm

def test_alarm_manager_connection(alarm_manager, mock_sio_client):
    # Assuming connect is called within the constructor
    mock_sio_client().connect.assert_called_once_with("http://127.0.0.1:5000/")

def test_adding_and_removing_alarms(alarm_manager, mock_alarm):
    alarm_manager.add_alarm(mock_alarm)
    assert mock_alarm in alarm_manager.alarms

    alarm_manager.remove_alarm(mock_alarm)
    assert mock_alarm not in alarm_manager.alarms


    


