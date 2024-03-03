import pytest
import sys
sys.path.append("src")

from flaskr import create_app

#This is a fixture that will be used to test the app
@pytest.fixture
def app():

    app = create_app({
        'TESTING': True,
    })

    yield app

#This is a class that will be used to test the login functionality
class AuthActions(object):
    def __init__(self, client):
        self._client = client

    #The login function will be used to test the login functionality
    def login(self, username='test', password='test'):
        return self._client.post(
            '/auth/login',
            data={'username': username, 'password': password}
        )

#This is a fixture that will be used to test the client
@pytest.fixture
def client(app):
    return app.test_client()

#This is a fixture that will be used to test the login functionality
@pytest.fixture
def auth(client):
    return AuthActions(client)