import sys
from flask_login import current_user, logout_user
sys.path.append("src")
import flaskr.register as register
import flaskr.login as login


def test_login(app):
    with app.test_request_context():
        assert not current_user.is_authenticated
        assert current_user.is_anonymous
        form = register.RegistrationForm()
        form.register("TestUser", "Test", "Test")
        loginForm = login.LoginForm()
        assert loginForm.login("TestUser", "Test")
        assert current_user.is_authenticated
        logout_user()
        assert not current_user.is_authenticated
        assert current_user.is_anonymous







