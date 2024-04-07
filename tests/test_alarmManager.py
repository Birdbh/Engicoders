import pytest
import sys
sys.path.append("src")
from sensors.alarm import Alarm
from alarmManager import AlarmManager

def test_AddRemoveAlarms():
    alarm1 = Alarm(500, 50, 1)
    alarm2 = Alarm(200, 100, -1)
    AlarmManager.addAlarm(alarm1)
    AlarmManager.addAlarm(alarm2)
    assert len(AlarmManager.getAlarmList()) == 2
    AlarmManager.removeAlarm(alarm1)
    assert len(AlarmManager.getAlarmList()) == 1


def test_singleton():
    alarm1 = Alarm(500, 50, 1)
    alarm2 = Alarm(200, 100, -1)
    AlarmManager.addAlarm(alarm1)
    AlarmManager.addAlarm(alarm2)
    alarmMan2 = AlarmManager()
    assert AlarmManager.getAlarmList() == alarmMan2.listofAlarms

def test_notify():
    alarm1 = Alarm(500, 50, 1)
    alarm2 = Alarm(200, 100, -1)
    AlarmManager.addAlarm(alarm1)
    AlarmManager.addAlarm(alarm2)
    AlarmManager.notifyAlarm(300)
    assert not alarm1.triggered() 
    assert not alarm2.triggered()
    AlarmManager.notifyAlarm(600) 
    assert alarm1.triggered() 
    assert not alarm2.triggered()
    AlarmManager.notifyAlarm(100) 
    assert alarm1.triggered() 
    assert alarm2.triggered()
    AlarmManager.clearAlarms()
    assert not alarm1.triggered() 
    assert not alarm2.triggered()

def test_getTriggers():
    AlarmManager.clearAll()
    alarm1 = Alarm(500, 50, 1)
    alarm2 = Alarm(200, 100, -1)
    AlarmManager.addAlarm(alarm1)
    AlarmManager.addAlarm(alarm2)
    assert AlarmManager.getTriggers() == [500, 200]





    


