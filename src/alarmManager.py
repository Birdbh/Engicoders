


from sensors.alarm import Alarm

import socketio

class AlarmObserver:
    def update(self, sensor):
        pass  # To be implemented

class AlarmManager(AlarmObserver):
    def __init__(self, server_address="http://127.0.0.1:5000/"):
        self.server_address = server_address
        self.sio = socketio.Client()
        self.connect()

    def connect(self):
        try:
            self.sio.connect(self.server_address)
        except socketio.exceptions.ConnectionError:
            pass  # Consider logging this

    def update(self, sensor, status, value):
        # Prepare the message
        if status == 'high':
            message = f"High alarm triggered for {sensor.get_name()}: Current value ({value}) is above the high threshold."
        elif status == 'low':
            message = f"Low alarm triggered for {sensor.get_name()}: Current value ({value}) is below the low threshold."
        
        print(message)
        message = f"Alarm triggered for {sensor.get_name()} with current value: {sensor.get_value()}."
        self.sio.emit('alarm_triggered', {'message': message})

    def disconnect(self):
        self.sio.disconnect()
