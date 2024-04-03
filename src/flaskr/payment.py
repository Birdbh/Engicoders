from flaskr.db import get_db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, DateField
from wtforms.validators import DataRequired

from flask import flash
from flaskr.db import get_db
from flask_login import current_user
import datetime

class PaymentForm(FlaskForm):
    CreditCard = IntegerField('16 Digit Credit Card Number', validators=[DataRequired()])
    ExpirationDate = DateField('Expiration Date')
    CardName = StringField('Name on Card', validators=[DataRequired()])
    SecurityDigits = IntegerField('3 Digit Security Code', validators=[DataRequired()])
    submit = SubmitField('Upgrade!')

    def validate_CreditCardNumber(self, CreditCard):
         
        if(CreditCard > 999999999999999 and CreditCard < 10000000000000000):
            return True
        flash("Invalid card number (AMEX NOT ACCEPTED)")
        return False

    def validate_Expiration(self, ExpirationDate):
        if(ExpirationDate > datetime.datetime.now().date()):
            return True
        flash("Expired Card, please enter a newer card")
        return False
    
    def validate_Security(self, SecurityCode):
        if(SecurityCode > 99 and SecurityCode < 1000):
            return True
        print(SecurityCode)
        return False
    def pay(self, CreditCard, ExpirationDate, SecurityCode): 
        db = get_db()
        if(self.validate_CreditCardNumber(CreditCard) and (self.validate_Expiration(ExpirationDate)) and (self.validate_Security(SecurityCode))):
            db.execute("Insert into payment (userid, CardNumber, amount) values (?,?, ?)", (current_user.get_id(), CreditCard, 99.99))
            db.commit()
            return True
        return False


        
