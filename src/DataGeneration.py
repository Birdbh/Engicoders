import requests
from datetime import datetime, timedelta
import requests
import json


#Documentation
#https://www.mathworks.com/help/thingspeak/readdata.html#mw_25e0bdab-cafa-48d4-84f5-5fce55aa281b

class DataGeneration:
    def __init__(self, channel_id, time_increment, field_number, start_date):
        self.channel_id = channel_id
        self.time_increment = time_increment
        self.field_number = field_number

        # Check if start_date is already a datetime object
        if isinstance(start_date, datetime):
            self.start_date = start_date
        else:
            # Try to parse the start_date string to datetime
            try:
                self.start_date = datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                raise ValueError("start_date must be a datetime object or a string in the format 'YYYY-MM-DD HH:MM:SS'")

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
    
    def fetch_thingspeak_data(self):
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
        start_date_str = self.start_date.strftime('%Y-%m-%d %H:%M:%S')

        start_date_formatted = start_date_str.replace(" ", "%20")


        # Construct the URL for the API request
        url = f"https://api.thingspeak.com/channels/{self.channel_id}/fields/{self.field_number}.json?start={start_date_formatted}&average={self.time_increment}"
        
        # Make the GET request to the ThingSpeak API
        response = requests.get(url)
        
        # Check if the request was successful
        if response.status_code == 200:
            return response.json()  # Return the parsed JSON response
        else:
            raise Exception("Thinkspeak request status code not equal to 200, verify channel & field id")  # Or handle errors as appropriate for your application
        
    def parse_json(self, json_data):
        
        parsed_json = {}
        for entry in json_data['feeds']:
            parsed_json[datetime.strptime(entry['created_at'], '%Y-%m-%dT%H:%M:%SZ')] = entry[f'field{self.field_number}']

        return parsed_json
    
    #def cleanse_data():



data = DataGeneration(9, 20, 1, "2023-03-01 00:00:00")
jsons = data.fetch_thingspeak_data()
print(data.parse_json(jsons))


#common request https://api.thingspeak.com/channels/{channel_id}/fields/{field_number}.json?start={YYYY-MM-DD%20HH:NN:SS.}&average={increment}
