from sensors.alarm import Alarm
#TODO have this store the global alarm list

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


