class SensorDataProcessor:
    def process_data(self):
        pass

class SensorDataDecorator(SensorDataProcessor):
    def __init__(self, sensor):
        self.sensor = sensor

    def __getattr__(self, name):
        "Delegate attribute access to the decorated sensor object"
        return getattr(self.sensor, name)

    def process_data(self):
        self.sensor.process_data()