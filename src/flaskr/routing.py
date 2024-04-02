
from flask import render_template, redirect, flash
from flaskr import app
from flaskr.register import RegistrationForm
from flaskr.login import LoginForm
from flaskr.upgrade import upgrade as upgradeF
from flask_login import logout_user, current_user

from sensors.sensor import Sensor
from flaskr.home import HomeForm
from flaskr.payment import PaymentForm
from Chart import Chart
from sensors.alarm import Alarm
from alarmManager import AlarmManager

@app.route('/')
@app.route('/index')
def index():
    if current_user.is_authenticated:
        return redirect('/home')
    else:
        return render_template('main/welcome.html')

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


@app.route('/upgrade', methods=['GET', 'POST'])
def upgrade():
    
    form = PaymentForm()  
    
    if form.validate_on_submit():
        if form.pay(form.CreditCard.data, form.ExpirationDate.data, form.SecurityDigits.data):
            return redirect('/upgrading')
    return render_template('main/upgrade.html', title='Upgrade', form=form)

@app.route('/upgrading')
def upgrading():
    upgradeF()
    return redirect('/')


@app.route('/home', methods=['GET', 'POST'])
def home():
    if not current_user.is_authenticated:
        return render_template('main/welcome.html')
    form = HomeForm()

    if form.is_submitted():

        if form.conflicting_input():
            flash('Only Channel ID, Field ID, Start Date, Time Increment OR Data Upload Must be Provided')
            return render_template('main/home.html')
        
        date_series, value_series = form.get_time_series_data()
                
        sensor = Sensor(name="Generated Sensor", description="Data from ThingSpeak", date_range=date_series, value=value_series)

        sensor = form.apply_data_modifiers(sensor)
        if form.alarm_min.data is not None and form.alarm_max.data is not None:
            # Initialize the Alarm with both the minimum and maximum thresholds
            sensor_alarm = Alarm(sensor, form.alarm_min.data, deadband=(form.alarm_max.data - form.alarm_min.data))
            sensor_alarm.register_observer(AlarmManager())
            sensor_alarm.set_alarm()

        chart = Chart(sensor)


        return render_template('main/home.html', labels=chart.get_labels(), values=chart.get_values(), chart_type=form.chartType.data)
    return render_template('main/home.html')

