import sys 
sys.path.append("src")

from sensors.DecoratorPattern import SensorDataDecorator

class cleanser(SensorDataDecorator):
    def __init__(self, sensor, deviations):
        super().__init__(sensor)
        self.deviations = deviations

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
        for i in range(len(data)):
            if data[i] > high:
                if i == 0:
                    data[i] = 0
                else:
                    data[i] = data[i-1]
            elif data[i] < low:
                if i == 0:
                    data[i] = 0
                else:
                    data[i] = data[i-1]
            else:
                pass
        return data

    def get_max(self):
        data = self.sensor.get_value()
        n=0
        for i in range(len(data)):
            if data[i]>=n:
                n=data[i]
            else:
                pass
        return n
    
    def get_min(self):
        data = self.sensor.get_value()
        n=self.get_max()
        for i in range(len(data)):
            if data[i]<=n:
                n=data[i]
            else:
                pass
        return n

    def remove_max(self):
        data = self.sensor.get_value()
        max = self.get_max()
        for i in range(len(data)):
            if data[i] == max and i==0:
                data[i] = 0
            elif data[i] == max:
                data[i] = data[i-1]
            else:
                pass
        return data
    
    def remove_min(self):
        data = self.sensor.get_value()
        min = self.get_min()
        for i in range(len(data)):
            if data[i] == min and i==0:
                data[i] = 0
            elif data[i] == min:
                data[i] = data[i-1]
            else:
                pass
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
    
    def process_data(self):
        super().process_data()
        self.replace_missing_values()
        self.set_data_types_to_float()
        self.remove_outlier()
        X = self.sensor.get_date_range()
        Y = self.sensor.get_value()
        return X, Y




