
from flask import render_template, redirect, flash, request, url_for
from flaskr import app
from flaskr.register import RegistrationForm
from flaskr.login import LoginForm
from flask_login import logout_user, current_user

import sys 
sys.path.append("src")
from DataGeneration import DataGeneration
from Chart import Chart
from sensors.sensor import Sensor

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect('/')
    form = LoginForm()
    if form.validate_on_submit():
        if(form.login(form.username.data, form.password.data)):
            return redirect('/')
    return render_template('auth/login.html', title='Log in', form=form)
@app.route('/logout')
def logout():
    logout_user()
    return redirect(('/'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.register(form.username.data, form.password.data, form.password2.data):
            return redirect('/')
        
    return render_template('auth/register.html', title='Register', form=form)

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
        except Exception as e:
            flash(f"Error while generating data: {e}")  # Use flash for error messages
            return redirect(url_for('home'))

        # Initialize Sensor with fetched data and pass data to the template for rendering
        sensor = Sensor("Generated Sensor", "Data from ThingSpeak", date_series, value_series)

        chart = Chart(sensor)

        return render_template('main/home.html', labels=chart.get_labels(), values=chart.get_values())

    return render_template('main/home.html')




