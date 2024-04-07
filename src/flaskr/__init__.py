import os
from flask import Flask
from flask_login import LoginManager
from flaskr.user import User, SuperUser




def create_app(test_config=None):
    # create and configure the app
    global app
    app = Flask(__name__, instance_relative_config=True)
    from . import db, routing, home
    login = LoginManager(app)
    
    #configuration is pulled from Flask Documentation
    app.config.from_mapping(
        SECRET_KEY='test_change_later',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )
    app.config['UPLOAD_FOLDER'] = os.path.join(app.instance_path, 'uploads')

    #ensure the instance folder exists (Based on Tutorial directions)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    app.app_context().push()
    
    
    #part of app, this guides the login and user. 
    @login.user_loader
    def load_user(id):
        try:
            if db.get_db().execute("SELECT id from PremiumUser where userid = (?)", (id,)).fetchone()['id'] > 0:
                return SuperUser(userid=id)
        except Exception as a:
            print(a)
            return User(userid=id)
        
    return app