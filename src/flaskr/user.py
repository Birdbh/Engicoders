from flask_login import UserMixin
import flaskr.db as db
from hashlib import sha512

class User(UserMixin):
    database = None
    username = ""
    userid = ""
    password = ""


    def __init__(self, username="", userid="", password=""): 
        self.database = db.get_db()
        if(userid != ""):
            self.set_userid(userid)
            try:
                self.set_username(self.database.execute("SELECT username from user where id = (?)", (userid,)).fetchone()['username'])
            except:
                self.set_username = ""
        elif(username != ""):
            self.set_username(username)
            self.set_userid(self.database.execute("SELECT id from user where username = (?)", (username,)).fetchone()['id'])
        
        
        

    def get_id(self):
        return self.userid
    def get_username(self):
        return self.username
    
    def set_username(self, username):
        self.username = username
    def set_userid(self, userid): 
        self.userid = userid

class SuperUser(User): 
    premium_features = True
    payment = ""
    

    def __init__(self, username="", userid="", password="", payment=""):
        super().__init__(username=username, userid=userid, password=password)
        
        #set_payment
    def upgrade(self):
        self.hash_password()

    def hash_password(self):
        hasher = sha512()
        password = str(self.database.execute("SELECT password from user where username = (?)", (self.username,)).fetchone()['password'])
        hasher.update(password.encode())
        self.password = hasher.hexdigest()
        self.database.execute("UPDATE user set password = (?) where username = (?)", (self.password, self.username))
        self.database.commit()
    
    def get_password(self):
        return self.password
        
    #def get_payment():
        #implement payment dw
    # def set_payment():
    #     #implement
    
