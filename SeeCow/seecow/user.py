# REf: https://github.com/shekhargulati/flask-login-example/blob/master/flask-login-example.py


from flask_login import UserMixin


class User(UserMixin):

    def __init__(self, id,username,password):
        self.id = id
        self.username = username
        self.password = password
        
    def __repr__(self):
        return "%d/%s/%s" % (self.id, self.name, self.password)
