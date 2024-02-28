import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

#Blueprint based on Flask Doc for the authorization page which wll include the login and registration systems
bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    #Functionality goes here
    return render_template('auth/login.html')