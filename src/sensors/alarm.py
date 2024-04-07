class Alarm:
    def __init__(self, threshold : float, deadband, HigherLower):
        self.threshold = threshold
        self.HigherLower = int(HigherLower)
        self.deadband = deadband*self.HigherLower
        
        self.delay = 0
        self.Occurances = 0
        self.is_set = False
        self.alarm_triggered = False
        self.trigger_time = None
        self.observers = []  # List of observers to be notified upon alarm

    def set_alarm(self):
        self.is_set = True
        self.alarm_triggered = False
        self.trigger_time = None

    def clear_alarm(self):
        self.Occurances = 0
        self.alarm_triggered = False


    def trigger_alarm(self):
        self.alarm_triggered = True


    def check(self, value):
        if self.HigherLower > 0 and value > self.threshold:
            self.trigger_alarm()
            self.Occurances = self.Occurances + 1
        elif self.HigherLower < 0 and value < self.threshold:
            self.trigger_alarm()
            self.Occurances = self.Occurances + 1




    #Table Attributes
    def getOccurances(self):
        return self.Occurances
    def triggered(self):
        return self.alarm_triggered
    def getLevel(self):
        return self.threshold
    def getHighLow(self):
        if self.HigherLower > 0:
            return "High"
        else:
            return "Low"
