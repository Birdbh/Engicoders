import os
from flask import Flask

from . import auth, db
app = Flask(__name__, instance_relative_config=True)

from flaskr import routing

def create_app(test_config=None):
    # create and configure the app
    

    #configuration is pulled from Flask Documentation
    app.config.from_mapping(
        SECRET_KEY='test_change_later',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    app.config.from_pyfile('config.py', silent=True)

    #ensure the instance folder exists (Based on Tutorial directions)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    app.register_blueprint(auth.bp)
    
    db.init_app(app)
    app.app_context().push()
    return app

        

    