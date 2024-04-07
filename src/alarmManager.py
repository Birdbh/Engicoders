from sensors.alarm import Alarm

class AlarmManager():
    listofAlarms = []

    def getAlarmList():
        return AlarmManager.listofAlarms

    def addAlarm(Alarm : Alarm):
        AlarmManager.listofAlarms.append(Alarm)
    def removeAlarm(Alarm : Alarm):
        AlarmManager.listofAlarms.remove(Alarm)

    def notifyAlarm(value):
        for alarm in AlarmManager.listofAlarms:
            alarm.check(value)
    def clearAlarms():
        for alarm in AlarmManager.listofAlarms:
            alarm.clear_alarm()
    def getTriggers():
        Triggers = []
        for alarm in AlarmManager.listofAlarms:
            Triggers.append(alarm.getLevel())
        return Triggers
    


