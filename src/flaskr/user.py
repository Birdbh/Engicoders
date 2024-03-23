from flask_login import UserMixin
import db
class User(UserMixin):
    database = None
    username = ""
    userid = ""
    is_authenticated = False
    is_active = False
    is_anonymous = False

    def User(self): 
        self.database = db.get_db()
        self.username = ""
        
        

    def get_id(self):
        return 0
    def get_username(self):
        return self.username
    def set_username(self, username):
        self.username = username
    def set_userid(self, userid): 
        self.userid = database

    def register(self, userid, username):
        self.set_userid(self.database.execute("SELECT userid from user where username = (?)", (username,)))