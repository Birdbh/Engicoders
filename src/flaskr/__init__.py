import os
from flask import Flask
from flask_login import LoginManager
from flaskr.user import User



def create_app(test_config=None):
    # create and configure the app
    global app
    app = Flask(__name__, instance_relative_config=True)
<<<<<<< HEAD
    from . import db, routing
    login = LoginManager(app)
    @login.user_loader
    def load_user(id):
        return User(userid=id)
=======
    from . import auth, db, routing, home

>>>>>>> ab13948 (working home.py :D init class also updated)
    #configuration is pulled from Flask Documentation
    app.config.from_mapping(
        SECRET_KEY='test_change_later',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    #app.config.from_pyfile('config.py', silent=True)
    
    #ensure the instance folder exists (Based on Tutorial directions)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    
    db.init_app(app)
    app.app_context().push()
    
    return app





        

    