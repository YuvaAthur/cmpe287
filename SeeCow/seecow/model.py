# REf: https://github.com/shekhargulati/flask-login-example/blob/master/flask-login-example.py

from seecow import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime



class User(UserMixin, db.Model):

    id              = db.Column(db.Integer,     primary_key=True)
    username        = db.Column(db.String(64),  unique = True)
    password   = db.Column(db.String(500))

    def __init__(self, username, password):
        self.username      = username
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


class Cattle(db.Model):
    id              = db.Column(db.Integer, primary_key=True) #auto-increment is on by default
    face_id         = db.Column(db.LargeBinary)
    dob             = db.Column(db.DateTime)
    origin          = db.Column(db.String(64))
    gender          = db.Column(db.String(8)) # Bull / Cow / Calf

    def __init__(self,face_id,dob,origin,gender):
        self.face_id = face_id
        self.dob = dob
        self.origin = origin
        self.gender = gender

    def __repr__(self):
        return "< Cattle ID %d / Origin %s / Gender %s>" %(self.id,self.origin,self.gender)

class Parlor(db.Model):
    id              = db.Column(db.Integer, primary_key=True) #auto-increment is on by default
    name            = db.Column(db.String(64))
    capacity        = db.Column(db.String(64))
    location        = db.Column(db.String(64))

    def __init__(self, name, capacity,location):
        self.name = name
        self.capacity = capacity
        self.location = location

    def __repr__(self):
        return "<Parlor Id %d / Name %s / Capacity %s / Location %s >" % (self.id, self.name,self.capacity,self.location)
    
class CattleMovement(db.Model):
    id              = db.Column(db.Integer, primary_key=True) #auto-increment is on by default
    cattle_id       = db.Column(db.Integer)
    parlor_id       = db.Column(db.Integer)
    date_time       = db.Column(db.DateTime)
    direction       = db.Column(db.String(8)) # IN / OUT

    def __init__(self, cattle_id, parlor_id,date_time,direction):
        self.cattle_id = cattle_id
        self.parlor_id = parlor_id
        self.date_time = date_time
        self.direction = direction


    def __repr__(self):
        return "<Movement Id %d / Cattle Id %s / Parlor Id %s /  Direction %s >" % (self.id,self.cattle_id, self.parlor_id,self.direction)
     






