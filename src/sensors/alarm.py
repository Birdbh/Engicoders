class Alarm:
    def __init__(self, threshold : float, deadband, HigherLower):
        self.threshold = threshold
        self.HigherLower = int(HigherLower)
        self.deadband = deadband*self.HigherLower
        self.TriggerLog = []
        self.delay = 0
        self.Occurances = 0
        self.is_set = False
        self.alarm_triggered = False
        self.trigger_time = None
        self.observers = []  # List of observers to be notified upon alarm

    def clear_alarm(self):
        self.Occurances = 0
        self.alarm_triggered = False


    def trigger_alarm(self):
        self.alarm_triggered = True


    def check(self, value):
        if self.HigherLower > 0 and float(value[0]) > self.threshold:
            self.trigger_alarm()
            self.Occurances = self.Occurances + 1
            self.logOccurance(value)
        elif self.HigherLower < 0 and float(value[0]) < self.threshold:
            self.trigger_alarm()
            self.Occurances = self.Occurances + 1
            self.logOccurance(value)

    def logOccurance(self, value):
        self.TriggerLog.append(value)
    
    def getLog(self):
        return self.TriggerLog

    #Table Attributes
    def getOccurances(self):
        return self.Occurances
    def triggered(self):
        return self.alarm_triggered
    def getLevel(self):
        return self.threshold
    def getHighLow(self):
        if self.HigherLower > 0:
            return 'High'
        else:
            return 'Low'
