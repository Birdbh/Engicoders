import pytest
from unittest.mock import MagicMock, patch
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

@pytest.mark.skip(reason="This test is currently being debugged")
def test_alarm_trigger_handling(alarm_manager, mock_alarm, mock_sio_client):
    # Add the mock alarm to the alarm manager
    alarm_manager.add_alarm(mock_alarm)
    
    # Simulate the alarm being triggered by manually calling the on_trigger callback
    alarm_manager.handle_alarm_trigger = MagicMock()

    # Pretend that the alarm condition is met, which should trigger the on_trigger method
    mock_alarm.check_sensor.side_effect = lambda: alarm_manager.handle_alarm_trigger(mock_alarm.sensor)

    # Run the alarm check, which should trigger the mock_alarm's on_trigger side effect
    alarm_manager.check_alarms()
    
    # Verify that handle_alarm_trigger was called
    alarm_manager.handle_alarm_trigger.assert_called_once_with(mock_alarm.sensor)

    # Assuming handle_alarm_trigger should emit a socketio message,
    # verify that emit was called with the appropriate event and message
    expected_message = f"Alarm triggered for {mock_alarm.sensor.get_name()} with current value: {mock_alarm.sensor.get_value()}."
    mock_sio_client().emit.assert_called_once_with('alarm_triggered', {'message': expected_message})


