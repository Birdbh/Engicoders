from sensors.sensor import Sensor

class Alarmer():
    def __init__(self, sensor: Sensor, highThreshold: float, lowThreshold: float):
        self.sensor = sensor
        self.highThreshold = highThreshold
        self.lowThreshold = lowThreshold
    
    def get_high_threshold(self):
        ht = []
        for i in range(len(self.sensor.get_value())):
            ht.append(self.highThreshold)
        return ht
    
    def get_low_threshold(self):
        lt = []
        for i in range(len(self.sensor.get_value())):
            lt.append(self.lowThreshold)
        return lt
