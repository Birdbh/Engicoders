class Alarm:
    def __init__(self, sensor, threshold, importance):
        """
        Initializes the Alarm.
        """
        self.sensor = sensor
        self.threshold = threshold
        self.importance = importance
        self.is_set = False

    def set_alarm(self):
        """
        Sets the alarm.
        """
        self.is_set = True
        print(f"Alarm for {self.sensor.get_name()} is set at threshold {self.threshold}.")

    def check_sensor(self):
        """
        Checks the sensor value against the threshold and triggers an alarm if necessary.
        """
        if self.is_set and self.sensor.get_value() > self.threshold:
            self.alert_alarm()

    def alert_alarm(self):
        """
        Triggers the alarm.
        """
        print(f"Alarm! {self.sensor.get_name()} has exceeded the threshold with a value of {self.sensor.get_value()}.")

    def delete_alarm(self):
        """
        Deletes the alarm.
        """
        self.is_set = False
        print(f"Alarm for {self.sensor.get_name()} is deleted.")

    def change_threshold(self, new_threshold):
        """
        Changes the threshold value of the alarm.
        """
        self.threshold = new_threshold
        print(f"Alarm threshold for {self.sensor.get_name()} is changed to {self.threshold}.")
