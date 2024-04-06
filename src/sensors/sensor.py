import sys 
sys.path.append("src")

from sensors.DecoratorPattern import SensorDataProcessor

class Sensor(SensorDataProcessor):
    def __init__(self, name, description, date_range, value):
        self.name = name
        self.description = description

        self.date_range = date_range
        self.value = value
        
        self.forcasted_values = []
        self.forcasted_date_range = []

    def __str__(self):
        return f"NAME:{self.name}, DESCRIPTION:{self.description}, DATE-RANGE:{self.date_range}, VALUES:{self.value}"
    
    def set_name(self, new_name):
        self.name = new_name
    
    def get_name(self):
        return self.name

    def set_description(self, new_description):
        self.description = new_description
    
    def get_description(self):
        return self.description

    def set_value(self, new_value):

        self.value = new_value

    def get_value(self):
        return self.value

    def set_date_range(self, new_date_range):
        self.date_range = new_date_range

    def get_date_range(self):
        return self.date_range

    def set_forecast_values(self, forcasted_values):
        self.forcasted_values = forcasted_values

    def get_forecast_values(self):
        return self.forcasted_values
    
    def set_forecast_date_range(self, forcasted_date_range):
        self.forcasted_date_range = forcasted_date_range
    
    def get_forecast_date_range(self):
        return self.forcasted_date_range
    
    def process_data(self):
        X = self.get_date_range()
        Y = self.get_value()
        for out in Y:
            self.notify(float(out))
        return X, Y

    
