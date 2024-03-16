import logging
import socketio


class Alarm:
    def __init__(self, sensor, threshold, importance):
        self.sensor = sensor
        self.threshold = threshold
        self.importance = importance
        self.is_set = False
        # Initialize Socket.IO client
        self.sio = socketio.Client(logger=True, engineio_logger=True)
        try:
            self.sio.connect('http://127.0.0.1:5000/')
        except socketio.exceptions.ConnectionError as e:
            logging.error(f"Failed to connect to Socket.IO server: {e}")

    def set_alarm(self):
        self.is_set = True
        self.log_message(f"Alarm for {self.sensor.get_name()} is set at threshold {self.threshold}.")

    def check_sensor(self):
        if self.is_set and self.sensor.get_value() > self.threshold:
            self.alert_alarm()

    def alert_alarm(self):
        message = f"Alarm! {self.sensor.get_name()} has exceeded the threshold with a value of {self.sensor.get_value()}."
        self.log_message(message)
        # Send the alarm message through Socket.IO
        self.sio.emit('alarm_message', {'message': message})

    def delete_alarm(self):
        self.is_set = False
        self.log_message(f"Alarm for {self.sensor.get_name()} is deleted.")

    def change_threshold(self, new_threshold):
        self.threshold = new_threshold
        self.log_message(f"Alarm threshold for {self.sensor.get_name()} is changed to {self.threshold}.")

    def log_message(self, message):
        logging.info(message)

    def disconnect(self):
        self.sio.disconnect()
