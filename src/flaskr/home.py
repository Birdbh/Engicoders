from flask import Flask, render_template, request, redirect, url_for, flash
import json
from Chart import Chart
from datetime import datetime
import sys
sys.path.append("src")
from sensors.sensor import Sensor
from DataGeneration import DataGeneration

from flaskr import app

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Extract form data
        channel_id = request.form.get('channel_id')
        field_id = request.form.get('field_id')
        start_date = request.form.get('start_date')
        time_increment = request.form.get('time_increment')

        # Initialize DataGeneration with form data
        try:
            data_gen = DataGeneration(channel_id, time_increment, field_id, start_date)
            date_series, value_series = data_gen.get_time_series()

            # Convert datetime objects in date_series to strings in ISO 8601 format
            date_series_str = [date.isoformat() if isinstance(date, datetime) else date for date in date_series]

        except Exception as e:
            flash(f"Error while generating data: {e}")  # Use flash for error messages
            return redirect(url_for('home'))
        
        sensor = Sensor(name="Generated Sensor", description="Data from ThingSpeak", date_range=date_series, value=value_series)
        chart = Chart(sensor)
        
        return render_template('main/home.html', labels=chart.get_labels(), values=chart.get_values())

    return render_template('main/home.html')
