import pytest
from unittest.mock import MagicMock
import sys
sys.path.append("src")
from sensors.alarm import Alarm

def test_create_alarm():
    alarm = Alarm(500, 50, 1)
    assert alarm.getHighLow() == 'High'
    assert alarm.getLevel() == 500
    assert alarm.getOccurances() == 0
    assert not alarm.triggered()

def test_triggerAlarm():
    alarm = Alarm(500, 50, 1)
    alarm.check(499)
    assert not alarm.triggered()
    assert not alarm.getOccurances() == 1
    alarm.check(501)
    assert alarm.triggered()
    assert alarm.getOccurances() == 1

def test_clearAlarm():
    alarm = Alarm(500, 50, 1)
    alarm.check(501)
    assert alarm.triggered()
    assert alarm.getOccurances() == 1
    alarm.clear_alarm()
    assert not alarm.triggered()
    assert alarm.getOccurances() == 0


