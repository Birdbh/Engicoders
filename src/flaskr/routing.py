
from flask import render_template, redirect, flash
from flaskr import app
from flaskr.register import RegistrationForm
from flaskr.login import LoginForm
from flask_login import logout_user, current_user

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
            if(LoginForm.login(LoginForm, form.username, form.password)):
                return redirect('/')
        
    return render_template('auth/register.html', title='Register', form=form)




