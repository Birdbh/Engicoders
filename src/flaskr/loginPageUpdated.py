#here's a basic example of an HTML Flask script for a login page with an option to create an account:

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dummy user database
users = {'user1': 'password1', 'user2': 'password2'}

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    
    if username in users and users[username] == password:
        return f'Welcome, {username}!'
    else:
        return 'Invalid username or password. <a href="/">Try again</a>.'

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/register', methods=['POST'])
def register():
    username = request.form['username']
    password = request.form['password']
    
    if username in users:
        return 'Username already exists. <a href="/signup">Try again</a>.'
    else:
        users[username] = password
        return f'Account created for {username}. <a href="/">Login</a>.'

if __name__ == '__main__':
    app.run()

#This script creates a Flask web application with routes for login, signup, and registration. 
#The login and signup forms use POST requests to submit data to the server, and the server checks the credentials against a dummy user database. 
#If the login is successful, it displays a welcome message, otherwise, it prompts the user to try again. 
#Similarly, the signup form checks if the username already exists and creates a new account if it doesn't.