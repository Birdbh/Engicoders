

import socketio
from sensors.alarm import Alarm

class AlarmManager:
    def __init__(self, server_address="http://127.0.0.1:5000/"):
        self.alarms = []
        self.server_address = server_address
        self.sio = socketio.Client()
        self.connect()

    def connect(self):
        """Connect to the Socket.IO server."""
        try:
            self.sio.connect(self.server_address)
        except socketio.exceptions.ConnectionError:
            # Handle connection error appropriately
            pass  # Consider logging this

    def add_alarm(self, alarm):
        """Add a new alarm to the manager."""
        if alarm not in self.alarms:
            self.alarms.append(alarm)
            alarm.on_trigger = self.handle_alarm_trigger

    def remove_alarm(self, alarm):
        """Remove an alarm from the manager."""
        if alarm in self.alarms:
            self.alarms.remove(alarm)

    def check_alarms(self):
        """Check each alarm; if triggered, the on_trigger callback will handle it."""
        for alarm in self.alarms:
            alarm.check_sensor()

    def handle_alarm_trigger(self, sensor):
        message = f"Alarm triggered for {sensor.get_name()} with current value: {sensor.get_value()}."
        self.sio.emit('alarm_triggered', {'message': message})

    def disconnect(self):
        """Disconnect from the Socket.IO server."""
        self.sio.disconnect()
