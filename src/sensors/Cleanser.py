import sys 
sys.path.append("src")

import sensors.sensor

class cleanser:
    def __init__(self, sensor, deviations):
        self.deviations = deviations
        self.sensor  = sensor

    def get_mean(self):
        data = self.sensor.get_value()
        length = len(data)
        tot = 0
        for i in range(len(data)):
            tot = tot + data[i]
        mean = tot / length
        return mean
    
    def get_standard_dev(self):
        mean = self.get_mean()
        data = self.sensor.get_value()
        n  = len(data)
        sum =0
        for i in range(len(data)):
            sum = sum+(data[i]-mean)**2
        dev = (sum/(n-1))**0.5
        return dev




    def remove_outlier(self):
        dev = self.deviations
        mean = self.get_mean()
        sdev = self.get_standard_dev()
        high = mean + dev*sdev
        low = mean - dev*sdev
        data = self.sensor.get_value()
        length = len(data)
        i=0
        while i<length:
            if data[i] > high:
                data.pop(i)
                length = length - 1
                i=i+1
            elif data[i] < low:
                data.pop(i)
                length = length -1
                i=i+1
            else:
                i=i+1
        return data
    
    def replace_missing_values(self):
        data = self.sensor.get_value()
        
        if data[0] == None:
                data[0] = 0
            
        for i in range(len(data)):
            if data[i] == None:
                data[i] = (data[i-1])

        self.sensor.set_value(data)

        return data

    def set_data_types_to_float(self):
        data = self.sensor.get_value()
        for i in range(len(data)):
            data[i] = float(data[i])

        self.sensor.set_value(data)
        return data




