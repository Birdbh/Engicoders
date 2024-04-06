from sensors.sensor import Sensor

class Chart():
    def __init__(self, sensor: Sensor, AlarmList):
        self.sensor = sensor
    
    def get_values(self):
        values = self.sensor.get_value()
        labels2 = []
        for i in range(len(values)):
            labels2.append(str(values[i]))
        return labels2
    
    def get_labels(self):
        labels = self.sensor.get_date_range()
        labels2 = []
        for i in range(len(labels)):
            labels2.append(str(labels[i]))
        return labels2

