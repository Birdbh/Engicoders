import flask_login
import flaskr.user as UserClass

def upgrade():
    user = flask_login.current_user
    user.premium_features = True
    user.set_username('aaa')
    user2 = UserClass.SuperUser(username=user.get_username(),userid=user.get_id())
    flask_login.logout_user()
    user2.upgrade()
    user2.premium_features = True
    user2.set_username('aaa')
    flask_login.login_user(user2, True)


