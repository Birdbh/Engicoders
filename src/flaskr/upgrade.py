import flask_login
import flaskr.user as UserClass

def upgrade():
    user = flask_login.current_user
    user = UserClass.SuperUser(username=user.get_username(),userid=user.get_id())
    flask_login.logout_user()
    user.upgrade()
    flask_login.login_user(user, True)


