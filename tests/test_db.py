import sqlite3
import pytest
import sys
sys.path.append("src")
from flaskr.db import get_db


def test_get_and_close_db(app):
   with app.app_context():
       db = get_db()
       assert db == get_db()


   with pytest.raises(sqlite3.ProgrammingError) as e:
       db.execute('SELECT 1')


   assert 'closed' in str(e.value)


#tests that get_db gets the right db
#also tests if the db is closed at the end


def test_init_db_command(runner, monkeypatch):
   class Recorder():
       called = False
  
   def fake_init_db():
       Recorder.called = True
  
   monkeypatch.setattr('src.flaskr.db.init_db', fake_init_db)
   result = runner.invoke(args=['init-db'])
   assert 'initialized' in result.output
   assert Recorder.called


#tests the flask new flask command init-db actually calls the init_db funciton
#monkey patch replaces the init_db function with the fake one that will record it being called
#runner calls the init-db command
