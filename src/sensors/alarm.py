class Alarm:
    def __init__(self, sensor, threshold, deadband=0, delay=0, on_trigger=None):
        self.sensor = sensor
        self.threshold = threshold
        self.deadband = deadband
        self.delay = delay
        self.is_set = False
        self.alarm_triggered = False
        self.trigger_time = None
        # Callback function to be called when alarm is triggered
        self.on_trigger = on_trigger

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
            return  # Alarm is not set, do nothing

        current_value = self.sensor.get_value()
        # Check if current value exceeds the threshold adjusted for the deadband
        if current_value > self.threshold + self.deadband:
            if not self.alarm_triggered:
                # If the alarm has not been triggered yet, start the timer
                if self.trigger_time is None:
                    self.trigger_time = time.time()
                # Check if the delay has passed since the alarm condition was met
                elif time.time() - self.trigger_time >= self.delay:
                    self.trigger_alarm()
        else:
            # If the current value is below the threshold or within the deadband, reset the alarm
            self.alarm_triggered = False
            self.trigger_time = None

    def trigger_alarm(self):
        self.alarm_triggered = True
        # Call the on_trigger callback
        if self.on_trigger:
            self.on_trigger(self.sensor)

    def is_alarm_active(self):
        return self.alarm_triggered
