import time

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
        if self.is_set:
            current_value = self.sensor.get_value()
            if current_value > self.threshold + self.deadband:
                if not self.alarm_triggered:
                    # If the alarm has not been triggered, start the timer
                    if self.trigger_time is None:
                        self.trigger_time = time.time()
                    # If the alarm has been triggered and the delay has passed, activate the alarm
                    elif time.time() - self.trigger_time >= self.delay:
                        self.trigger_alarm()
            else:
                # If the value is back in range, clear the alarm and reset the timer
                self.clear_alarm()

    def trigger_alarm(self):
        self.alarm_triggered = True
        # Instead of emitting directly, we now call the callback
        if self.on_trigger:
            self.on_trigger(self.sensor)

    def is_alarm_active(self):
        return self.alarm_triggered
