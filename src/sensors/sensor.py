class Sensor:
    def __init__(self, id, name, description, type, location, value):
        self.id = id
        self.name = name
        self.description = description
        self.type = type
        self.value = value

    def __str__(self):
        return f"Sensor: ID:{self.id}, NAME:{self.name}, DESCRIPTION:{self.description}, DATA-TYPE:{self.type}, {self.value}"