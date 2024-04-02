import sys
sys.path.append("src")

import flaskr.user as Userclass



def test_register(app):
    with app.test_request_context():
        user = Userclass.User("test")
        assert user.get_id() == 1
        assert user.get_username() == 'test'
        
