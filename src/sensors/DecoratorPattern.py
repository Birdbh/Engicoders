
class SensorDataProcessor:
    def process_data(self):
        pass

class SensorDataDecorator(SensorDataProcessor):
    def __init__(self, sensor_data_processor):
        self._sensor_data_processor = sensor_data_processor

    def process_data(self):
        self._sensor_data_processor.process_data()
