from flask import Blueprint, render_template, request, redirect, url_for
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import sys
sys.path.append("src")
from sensors.sensor import Sensor
from DataGeneration import DataGeneration


bp = Blueprint('home', __name__, url_prefix='/home')

@bp.route('/', methods=('GET', 'POST'))
def home():
    if request.method == 'POST':
        
        channel_id = request.form.get('channel_id')
        time_increment = request.form.get('time_increment')
        field_number = request.form.get('field_number')
        start_date = request.form.get('start_date')

        # Create DataGeneration
        try:
            data_gen = DataGeneration(channel_id, time_increment, field_number, start_date)
        except ValueError as e:
            return f"Error processing input data: {e}", 400

        # Fetch and process data
        try:
            time_series_data = data_gen.get_time_series()
        except Exception as e:
            return f"Error fetching data from ThingSpeak: {e}", 500

        # Create Sensor objects from the fetched data 
        sensors = []
        for timestamp, value in time_series_data.items():
            sensor = Sensor(id=None, name=f"Sensor {field_number}", description="Fetched from ThingSpeak", type="ThingSpeak Data", value=value)
            sensors.append(sensor)

        labels = [timestamp.strftime('%Y-%m-%d %H:%M:%S') for timestamp in time_series_data.keys()]
        values = [value for value in time_series_data.values()]

        
        return redirect(url_for('home.home'))
    else:
        
        return render_template('home.html')
