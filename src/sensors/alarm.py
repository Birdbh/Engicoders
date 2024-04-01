class Alarm:
    def __init__(self, sensor, threshold, deadband=0, delay=0):
        self.sensor = sensor
        self.threshold = threshold
        self.deadband = deadband
        self.delay = delay
        self.is_set = False
        self.alarm_triggered = False
        self.trigger_time = None
        self.observers = []  # List of observers to be notified upon alarm

    def register_observer(self, observer):
        self.observers.append(observer)

    def unregister_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self):
        for observer in self.observers:
            observer.update(self.sensor)

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

    def is_alarm_active(self):
        return self.alarm_triggered
