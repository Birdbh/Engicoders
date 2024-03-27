from flask import Flask, render_template, request, redirect, url_for, flash
import json
from Chart import Chart
from datetime import datetime
import sys
sys.path.append("src")
from sensors.sensor import Sensor
from DataGeneration import DataGeneration

import sys 
sys.path.append("src")

from sensors import sensor, Prediction, Cleanser

from flaskr import app

@app.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Extract form data
        channel_id = request.form.get('channel_id')
        field_id = request.form.get('field_id')
        start_date = request.form.get('start_date')
        time_increment = request.form.get('time_increment')
        is_cleanse = request.form.get('cleanse')
        is_predict = request.form.get('predict')
        prediction_date = request.form.get('prediction_date')
        chart_type = request.form.get('chartType')  # Retrieve the selected chart type
        stdDeviation = request.form.get('stdDeviation')
        print(type(stdDeviation))
        # Initialize DataGeneration with form data
        try:
            data_gen = DataGeneration(channel_id, time_increment, field_id, start_date)
            date_series, value_series = data_gen.get_time_series()

        except Exception as e:
            flash(f"Error while generating data: {e}")  # Use flash for error messages
            return redirect(url_for('home'))
        
        sensor = Sensor(name="Generated Sensor", description="Data from ThingSpeak", date_range=date_series, value=value_series)

        if is_cleanse == "on":
            stdDeviation = int(stdDeviation)
            sensor = Cleanser.cleanser(sensor, deviations=stdDeviation)

        if is_predict == "on":
            sensor = Prediction.DataPrediction(sensor, prediction_date)

        labels, values = sensor.process_data()
        sensor.set_date_range(labels)
        sensor.set_value(values)

        chart = Chart(sensor)
        return render_template('main/home.html', labels=chart.get_labels(), values=chart.get_values(), chart_type=chart_type)

    return render_template('main/home.html')
