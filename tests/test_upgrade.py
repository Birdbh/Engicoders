import sys
import flask_login
sys.path.append("src")
import flaskr.register as register
from flask_login import current_user
import flaskr.upgrade as upgrade
from hashlib import sha512



def test_upgrade(app):
     with app.test_request_context():
        form = register.RegistrationForm()
        form.register("TestUser2", "Test2", "Test2")
        user = flask_login.current_user
        upgrade.upgrade()
        assert user.premium_features == True
        assert not user.get_password() == "Test2"
        hasher = sha512()
        hasher.update(str.encode("Test2"))
        assert user.get_password() == hasher.hexdigest()

        