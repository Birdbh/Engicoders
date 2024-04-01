import flask_login
import flaskr.user as UserClass
from flaskr.db import get_db
import time
import datetime
from dateutil.relativedelta import relativedelta

def upgrade():
    db = get_db()
    
    user = flask_login.current_user
    try:
        db.execute("INSERT INTO PremiumUser (userid, expires) values (?, ?)", (user.get_id(), (datetime.datetime.today() + relativedelta(months=1))))
        db.commit()
    except:
        return
    user2 = UserClass.SuperUser(username=user.get_username(),userid=user.get_id())
    flask_login.logout_user()
    print(user)
    user2.upgrade()
    print(user2)
    user2.premium_features = True
    user2.set_username('aaa')
    flask_login.login_user(user2, True, force=True, fresh=True)
    user3 = flask_login.current_user
    print(user3)

    

