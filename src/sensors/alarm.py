class Alarm:
    def __init__(self, threshold, deadband, HigherLower):
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
        self.is_set = False
        self.alarm_triggered = False
        self.trigger_time = None

    def check_sensor(self):
        if not self.is_set:
            return

        current_value = self.sensor.get_value()

        if current_value > self.threshold + self.deadband:
            if not self.alarm_triggered:
                if self.trigger_time is None:
                    self.trigger_time = time.time()
                if self.delay == 0 or time.time() - self.trigger_time >= self.delay:
                    self.trigger_alarm()
        else:
            self.trigger_time = None

    def trigger_alarm(self):
        self.alarm_triggered = True
        self.notify_observers()


    def check(self, sensor, status, value):
        # Prepare the message
        if status == 'high':
            message = f"High alarm triggered for {sensor.get_name()}: Current value ({value}) is above the high threshold."
        elif status == 'low':
            message = f"Low alarm triggered for {sensor.get_name()}: Current value ({value}) is below the low threshold."
        
        print(message)
        message = f"Alarm triggered for {sensor.get_name()} with current value: {sensor.get_value()}."
        self.sio.emit('alarm_triggered', {'message': message})



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
