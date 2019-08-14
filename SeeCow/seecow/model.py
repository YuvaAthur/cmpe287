# REf: https://github.com/shekhargulati/flask-login-example/blob/master/flask-login-example.py

from seecow import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash



class User(UserMixin, db.Model):

    id              = db.Column(db.Integer,     primary_key=True)
    username        = db.Column(db.String(64),  unique = True)
    password   = db.Column(db.String(500))

    def __init__(self, username, password):
        self.username           = username
        self.password      = generate_password_hash(password)

    def __repr__(self):
        return "< User ID %d/ Username %s>" % (self.id, self.username)
        # return '<User %r>' % (self.id)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def save(self):

        # inject self into db session    
        db.session.add ( self )

        # commit change and save the object
        db.session.commit( )

        return self 

"""
CREATE TABLE parlor_status (
  id INTEGER PRIMARY_KEY,
  cattle_id TEXT,
  info TEXT NOT NULL,
  place TEXT NOT NULL,
  time TEXT
 );
"""        
class Parlor(db.Model):
    id              = db.Column(db.Integer, primary_key=True) #auto-increment is on by default
    cattle_id       = db.Column(db.String(64))
    info            = db.Column(db.String(64))
    place           = db.Column(db.String(64))
    time            = db.Column(db.DateTime)

    def __repr__(self):
        return '<Entry Id %d / Cattle Id %s / Info %s / Place %s / DateTime %s >' % self.id, self.cattle_id,self.info, self.place, self.time




"""
class User(UserMixin):

    def __init__(self, id,username,password):
        self.id = id
        self.username = username
        self.password = password
        
    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)

"""
