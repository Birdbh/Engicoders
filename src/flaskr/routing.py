
from flask import render_template, redirect, flash
from flaskr import app
from flaskr.register import RegistrationForm
from flaskr.login import LoginForm
from flask_login import logout_user, current_user

from sensors.sensor import Sensor
from flaskr.home import HomeForm
from Chart import Chart

@app.route('/')
@app.route('/index')
def index():
    return render_template('main/home.html')

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
    form = HomeForm()

    if form.is_submitted():

        if form.conflicting_input():
            flash('Only Channel ID, Field ID, Start Date, Time Increment OR Data Upload Must be Provided')
            return render_template('main/home.html')
    
        date_series, value_series = form.get_time_series_data()
                
        sensor = Sensor(name="Generated Sensor", description="Data from ThingSpeak", date_range=date_series, value=value_series)

        sensor = form.apply_data_modifiers(sensor)

        chart = Chart(sensor)


        return render_template('main/home.html', labels=chart.get_labels(), values=chart.get_values(), chart_type=form.chartType.data)
    return render_template('main/home.html')

