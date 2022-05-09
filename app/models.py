import email
from msilib.schema import Property
from . import db
from werkzeug.security import generate_password_hash , check_password_hash

#...

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
    emailaddress = db.Column(db.String(255))
    password_input = db.Column(db.String(255))
    
    @property
    def password(self, password):
        raise AttributeError('Error')
    @password.setter
    def password(self, password):
        self.password_input = generate_password_hash(password)

    def verify_password(self,password):
            return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'User {self.username}'

    