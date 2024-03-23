from flask_login import UserMixin
import flaskr.db as db
from hashlib import sha256

class User(UserMixin):
    database = None
    username = ""
    userid = ""
    password = ""
    is_authenticated = False
    is_active = False
    is_anonymous = False

    def __init__(self, username="", userid="", password=""): 
        self.database = db.get_db()
        self.set_username(username)
        self.set_userid(userid)
        self.password = password
        
        

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


class SuperUser(User): 
    premium_features = True
    hasher = sha256()

    def __init__(self, username="", userid="", password=""):
        super().__init__(username=username)
        self.upgrade()
    def upgrade(self):
        self.hash_password()

    def hash_password(self):
        password = self.database.execute("SELECT password from user where username = (?)", (self.username,)).fetchone()['password']
        print(password)
        self.hasher.update(str.encode(password))
        self.password = self.hasher.hexdigest()
        self.database.execute("UPDATE user set password = (?) where username = (?)", (self.password, self.username))
    
    def get_password(self):
        return self.password
        
    # def get_payment():
    #     #implement payment dw
    # def set_payment():
    #     #implement
    