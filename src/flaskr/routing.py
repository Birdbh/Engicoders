
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
        
        if form.conflicting_modifers():
            flash('Data Prediction Requires Data Cleansing')
            return render_template('main/home.html')
    
        try:
            date_series, value_series = form.get_time_series_data()

        except Exception as e:
            flash("A Valid Public Channel and Field ID Must be Provided")
            return render_template('main/home.html')
                
        sensor = Sensor(name="Generated Sensor", description="Data from ThingSpeak", date_range=date_series, value=value_series)

        sensor = form.apply_data_modifiers(sensor)

        chart = Chart(sensor)


        return render_template('main/home.html', labels=chart.get_labels(), values=chart.get_values(), chart_type=form.chartType.data)
    return render_template('main/home.html')

