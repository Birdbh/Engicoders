class Sensor:
    def __init__(self, id, name, description, type, value):
        self.id = id
        self.name = name
        self.description = description
        self.type = type
        self.value = value
        self.forcasted_values = {}

    #jesmes

    def __str__(self):
        return f"Sensor: ID:{self.id}, NAME:{self.name}, DESCRIPTION:{self.description}, DATA-TYPE:{self.type}, VALUES: {self.value}"
    
    def set_id(self, new_id):
        self.id = new_id

    def get_id(self):
        return self.id
    
    def set_name(self, new_name):
        self.name = new_name
    
    def get_name(self):
        return self.name

    def set_description(self, new_description):
        self.description = new_description
    
    def get_description(self):
        return self.description
    
    def set_type(self, new_type):
        self.type = new_type

    def get_type(self):
        return self.type

    def set_value(self, new_value):
        self.value = new_value

    def get_value(self):
        return self.value

    def set_forecast_values(self, forcasted_values):
        self.forcasted_values = forcasted_values

    def get_forecast_values(self):
        return self.forcasted_values
    


    
