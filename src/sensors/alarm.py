import time

class Alarm:
    def __init__(self, sensor, highThreshold, lowThreshold, deadband=0, delay=0, on_trigger=None):
        self.sensor = sensor
        self.highThreshold = highThreshold
        self.lowThreshold = lowThreshold
        self.deadband = deadband
        self.delay = delay
        self.is_set = False
        self.alarm_triggered = False
        self.trigger_time = None
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
            return
    
        current_value = self.sensor.get_value()
    
        if current_value > self.highThreshold + self.deadband:
            if not self.alarm_triggered:
                # Start the delay timer if it's not started yet
                if self.trigger_time is None:
                    self.trigger_time = time.time()
                # If there's no delay, or the delay has passed, trigger the alarm
                if self.delay == 0 or time.time() - self.trigger_time >= self.delay:
                    self.trigger_alarm()
        else:
            # Reset the trigger time if value falls below threshold or within deadband
            self.trigger_time = None

    def trigger_alarm(self):
        self.alarm_triggered = True
        # Call the on_trigger callback
        if self.on_trigger:
            self.on_trigger(self.sensor)

    def is_alarm_active(self):
        return self.alarm_triggered
    
    def get_high_threshold_list(self):
        ht = []
        for i in range(len(self.sensor.get_value())):
            ht.append(self.highThreshold)
        return ht
    
    def get_low_threshold_list(self):
        lt = []
        for i in range(len(self.sensor.get_value())):
            lt.append(self.lowThreshold)
        return lt
