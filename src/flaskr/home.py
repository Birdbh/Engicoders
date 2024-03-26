<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from flask import Flask, render_template, request, redirect, url_for, flash
=======
from flask import Flask, render_template, request, redirect, url_for
>>>>>>> c0aff6c (Integrate New Sensor Class into home/main.py)
=======
from flask import Flask, render_template, request, redirect, url_for, flash
>>>>>>> 41be2bc (home.html and home.py updated)
=======
from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
>>>>>>> 1d353de (modified for charts)
from datetime import datetime
import json
from flaskr import app
import sys
sys.path.append("src")
<<<<<<< HEAD
<<<<<<< HEAD
from sensors.sensor import Sensor 
from DataGeneration import DataGeneration


@app.route('/home', methods=['GET', 'POST'])
=======
from sensors.sensor import Sensor  # Adjust the import path as needed
=======
from sensors.sensor import Sensor 
>>>>>>> 41be2bc (home.html and home.py updated)
from DataGeneration import DataGeneration

from flaskr import app

<<<<<<< HEAD

app = Flask(__name__)  # Only if the Flask app instance is defined in this file

@app.route('/home', methods=['GET', 'POST'])  # Adjust the route as needed
>>>>>>> c0aff6c (Integrate New Sensor Class into home/main.py)
=======
@app.route('/', methods=['GET', 'POST'])
>>>>>>> 41be2bc (home.html and home.py updated)
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

            # Convert datetime objects in date_series to strings
            date_series_str = [date.isoformat() for date in date_series]
            date_series_str = [date.isoformat() if isinstance(date, datetime) else date for date in date_series]

        except Exception as e:
            flash(f"Error while generating data: {e}")
            return redirect(url_for('home'))


        except Exception as e:
<<<<<<< HEAD
<<<<<<< HEAD
            flash(f"Error while generating data: {e}")  # Use flash for error messages
            return redirect(url_for('home'))

        # Initialize Sensor with fetched data and pass data to the template for rendering
        sensor = Sensor(name="Generated Sensor", description="Data from ThingSpeak", date_range=date_series, value=value_series)
        labels_json=json.dumps(date_series_str)
    
        values_json=json.dumps(value_series)
        return render_template('main/home.html', labels=date_series, values=value_series)

    return render_template('main/home.html')
=======
            # Consider using Flask's flash messages to show errors on the web page
            return f"Error while generating data: {e}", 400
=======
            flash(f"Error while generating data: {e}")  # Use flash for error messages
            return redirect(url_for('home'))
>>>>>>> 41be2bc (home.html and home.py updated)

        # Initialize Sensor with fetched data and pass data to the template for rendering
        sensor = Sensor(name="Generated Sensor", description="Data from ThingSpeak", data={'dates': date_series, 'values': value_series})
        return render_template('main/home.html', labels=date_series, values=value_series)

<<<<<<< HEAD
        # Pass data to the template for rendering
        return render_template('home.html', labels=date_series, values=value_series)

    # For GET requests, just render the template
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)  # Consider removing debug=True for production
>>>>>>> c0aff6c (Integrate New Sensor Class into home/main.py)
=======
    return render_template('main/home.html')
>>>>>>> 41be2bc (home.html and home.py updated)
