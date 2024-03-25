import flask_login
from flaskr.user import SuperUser

def upgrade():
    user = flask_login.current_user
    flask_login.logout_user()
    user = SuperUser()
