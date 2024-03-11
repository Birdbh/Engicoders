import requests
from datetime import datetime, timedelta

#Documentation
#https://www.mathworks.com/help/thingspeak/readdata.html#mw_25e0bdab-cafa-48d4-84f5-5fce55aa281b

class DataGeneration:
    def __init__(self, channel_id, time_increment, field_number, start_date):
        self.channel_id = channel_id
        self.time_increment = time_increment
        self.field_number = field_number
        self.start_date = start_date

    def __str__(self):
        return f"DataGeneration: CHANNEL_ID:{self.channel_id}, TIME_INCREMENT:{self.time_increment}, FIELD_NUMBER:{self.field_number}, START_DATE:{self.start_date}"

    def set_channel_id(self, channel_id):
        self.channel_id = channel_id

    def get_channel_id(self):
        return self.channel_id
    
    def set_time_increment(self, time_increment):
        self.time_increment = time_increment

    def get_time_increment(self):
        return self.time_increment
    
    def set_field_number(self, field_number):
        self.field_number = field_number

    def get_field_number(self):
        return self.field_number
    
    def set_start_date(self, start_date):
        self.start_date = start_date

    def get_start_date(self): 
        return self.start_date


#common request https://api.thingspeak.com/channels/{channel_id}/fields/{field_number}.json?start={YYYY-MM-DD%20HH:NN:SS.}&average={increment}
'''
import requests

def fetch_thingspeak_data(channel_id, field_number, start_date, end_date, average_increment):
    """
    Fetches averaged data from a specific field of a ThingSpeak channel over a given time range.
    
    Parameters:
    - channel_id: str or int, the ID of the ThingSpeak channel.
    - field_number: str or int, the field number to fetch data from (1-8).
    - start_date: str, the start date and time in the format "YYYY-MM-DD HH:NN:SS".
    - end_date: str, the end date and time in the format "YYYY-MM-DD HH:NN:SS".
    - average_increment: str or int, the time increment in minutes over which to average the data.
    
    Returns:
    - A Python dictionary object containing the API response.
    """
    # Format the start and end date strings to fit the URL encoding
    start_date_formatted = start_date.replace(" ", "%20")
    end_date_formatted = end_date.replace(" ", "%20")
    
    # Construct the URL for the API request
    url = f"https://api.thingspeak.com/channels/{channel_id}/fields/{field_number}.json?start={start_date_formatted}&end={end_date_formatted}&average={average_increment}"
    
    # Make the GET request to the ThingSpeak API
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        return response.json()  # Return the parsed JSON response
    else:
        return None  # Or handle errors as appropriate for your application

# Example usage
channel_id = 'YOUR_CHANNEL_ID'  # Replace with your channel ID
field_number = 'FIELD_NUMBER'  # Replace with the field number you want to query
start_date = 'YYYY-MM-DD HH:MM:SS'  # Replace with your start date
end_date = 'YYYY-MM-DD HH:MM:SS'  # Replace with your end date
average_increment = 'INCREMENT'  # Replace with your desired average increment in minutes

# Fetch the data
data = fetch_thingspeak_data(channel_id, field_number, start_date, end_date, average_increment)
print(data)

'''