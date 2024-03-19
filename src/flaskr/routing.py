
from flask import render_template, redirect, flash
from flaskr import app
from flaskr.register import RegistrationForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        if form.register(form.username.data, form.password.data, form.password2.data):
            return redirect('/')
        
    return render_template('auth/register.html', title='Register', form=form)
