from sensors.sensor import Sensor

class Chart():
    def __init__(self, sensor: Sensor):
        self.sensor = sensor
    
    def get_values(self):
        return self.sensor.get_value()
    
    def get_labels(self):
        labels = self.sensor.get_date_range()
        labels2 = []
        for i in range(len(labels)):
            labels2.append(str(labels[i]))
        return labels2

