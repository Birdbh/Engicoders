#In this Flask code:
#The / route renders the login page.
#The /login route handles the form submission and checks if the provided username and password match the data in the users dictionary. If the login is successful, it redirects to the /success route; otherwise, it redirects back to the login page.
#The /success route simply displays a success message.

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Fake user data for demonstration purposes
users = {'user1': 'password1', 'user2': 'password2'}


@app.route('/')
def login_page():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if username in users and users[username] == password:
        # Successful login, redirect to a different page or do something else
        return redirect(url_for('success'))
    else:
        # Invalid login, redirect back to the login page with a message
        return redirect(url_for('login_page'))


@app.route('/success')
def success():
    return "Login successful!"


if __name__ == '__main__':
    app.run()
