from flask_login import UserMixin
import flaskr.db as db

class User(UserMixin):
    database = None
    username = ""
    userid = ""
    is_authenticated = False
    is_active = False
    is_anonymous = False

    def __init__(self, username="", userid=""): 
        self.database = db.get_db()
        self.set_username(username)
        self.set_userid(userid)
        
        

    def get_id(self):
        return self.userid
    def get_username(self):
        return self.username
    
    def set_username(self, username):
        self.username = username
    def set_userid(self, userid): 
        self.userid = userid

    def register(self, username):
        self.set_username(username)
        self.set_userid(self.database.execute("SELECT id from user where username = (?)", (username,)).fetchone()['id'])