import sys
sys.path.append("src")
import flaskr.register as register
import flaskr.db as dbClass




def test_register(app):
    with app.test_request_context():
        form = register.RegistrationForm()
        form.register("TestUser", "Test", "Test")
        db = dbClass.get_db()
        assert db.execute("SELECT username from user").fetchone()['username'] == "TestUser"
        assert db.execute("SELECT password from user where username = 'TestUser'").fetchone()['password'] == "Test"
        assert not (db.execute("SELECT password from user where username = 'TestUser'").fetchone()['password'] == "test")
        assert not (form.register("TestUser43", "Test", "test"))
        assert not (form.register("test", "Test", "Test"))
        



def test_validate_password():
    assert register.RegistrationForm.validate_pass(register.RegistrationForm, "Test", "Test")
    assert not (register.RegistrationForm.validate_pass(register.RegistrationForm, "Test", "test"))

def test_validate_username(app):
    with app.test_request_context():
        db = dbClass.get_db()
        assert register.RegistrationForm.validate_user(register.RegistrationForm, db, "Test")
        assert not (register.RegistrationForm.validate_user(register.RegistrationForm, db, ""))

