import pytest
import sys
import os
import tempfile
sys.path.append("src")


from flaskr import create_app
from flaskr.db import get_db, init_db


with open(os.path.join(os.path.dirname(__file__), 'data.sql'), 'rb') as f:
   _data_sql = f.read().decode('utf8')


#This is a fixture that will be used to test the app
@pytest.fixture
def app():
   db_fd, db_path = tempfile.mkstemp()


   app = create_app({
       'TESTING': True,
       'DATABASE': db_path,
   })


   with app.app_context():
       init_db()
       get_db().executescript(_data_sql)
   yield app


   os.close(db_fd)
   os.unlink(db_path)


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


#this is used to complete click commands
@pytest.fixture
def runner(app):
   return app.test_cli_runner()