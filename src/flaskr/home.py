from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import sys
sys.path.append("src")
from sensors.sensor import Sensor  # Adjust the import path as needed
from DataGeneration import DataGeneration


from flaskr import app


app = Flask(__name__)  # Only if the Flask app instance is defined in this file

@app.route('/home', methods=['GET', 'POST'])  # Adjust the route as needed
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
        except Exception as e:
            # Consider using Flask's flash messages to show errors on the web page
            return f"Error while generating data: {e}", 400

        # Assuming Sensor class can be initialized directly with the fetched data
        sensor = Sensor(name="Generated Sensor", description="Data from ThingSpeak", data={'dates': date_series, 'values': value_series})

        # Pass data to the template for rendering
        return render_template('home.html', labels=date_series, values=value_series)

    # For GET requests, just render the template
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)  # Consider removing debug=True for production
