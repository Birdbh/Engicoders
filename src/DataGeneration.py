import requests
from datetime import datetime, timedelta

class DataGeneration:
    def __init__(self, channel, time_increment):
        self.channel = channel
        self.time_increment = time_increment


print(requests.get('https://api.thingspeak.com/channels/9/feeds.json').json())