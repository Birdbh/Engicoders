import requests
from datetime import datetime, timedelta

#Documentation
#https://www.mathworks.com/help/thingspeak/readdata.html#mw_25e0bdab-cafa-48d4-84f5-5fce55aa281b

class DataGeneration:
    def __init__(self, channel, time_increment):
        self.channel = channel
        self.time_increment = time_increment
    
    def request_data(self):



print(requests.get('https://api.thingspeak.com/channels/9/feeds.json').json())

