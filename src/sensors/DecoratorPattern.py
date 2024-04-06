from alarmManager import AlarmManager
# Requires: This is an interface definition.

# Modifies: Not directly applicable

# Effects:
# Provides a contract for data processing operations. Implementing classes (Sensor, Cleanser, Prediction) must provide specific behaviors for processing sensor data.

class SensorDataProcessor:
    def process_data(self):
        pass
    
    def notify(self, value):
       AlarmManager.notifyAlarm(value)

# Requires:
# An instance of SensorDataProcessor that it decorates. This instance is expected to be a concrete component like Cleanser or Prediction.

# Modifies:
# Potentially modifies the state of the SensorDataProcessor instance it decorates through the process_date operations, depending on the specific implementation of the decorators (Cleanser, Prediction).

# Effects:
# Serves as a base for concrete decorators (Cleanser, Prediction) to extend the functionality of SensorDataProcessor objects dynamically.

# Delegates calls to the decorated SensorDataProcessor object, allowing for additional operations before or after this delegation as implemented by concrete decorators.

class SensorDataDecorator(SensorDataProcessor):
    def __init__(self, sensor):
        self.sensor = sensor

    def __getattr__(self, name):
        #Delegate attribute access to the decorated sensor object
        return getattr(self.sensor, name)

    def process_data(self):
        self.sensor.process_data()


    