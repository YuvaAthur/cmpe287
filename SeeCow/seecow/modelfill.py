# python script to fill database
# For running from commandline
# >>> python
# >>> exec(open("./seecow/modelfill.py").read())
# Preserves local variables!!

# initialize context & db
from seecow import create_app
app = create_app()
app.app_context().push()
from seecow import db
import seecow.model

# uncomment only to create an empty db
db.create_all()

# Create user records
from seecow.model import User
u = User('abc','abc')
db.session.add(u)
db.session.commit()

# Create cattle records
from seecow.model import Cattle
from datetime import datetime
from dateutil.parser import parse
d = parse('2014-05-01 18:47:05.069722')
c = Cattle(None,d,'Australian Jersey','Cow') # id = 1
db.session.add(c)
d = parse('2013-05-01 02:47:05.069722')
c = Cattle(None,d,'Punjab Ox','Bull') # id = 2
db.session.add(c) 
d = parse('2016-05-01 05:47:05.069722')
c = Cattle(None,d,'California Poppy','Cow') #id = 3
db.session.add(c) 
db.session.commit

# Create parlor records
from seecow.model import Parlor
p = Parlor('South',100,'south') # id = 1
db.session.add(p)
p = Parlor('North',50,'north') # id = 2
db.session.add(p)
db.session.commit()

# Add Movement records
from seecow.model import CattleMovement
m = CattleMovement(1,1,datetime.now(),'IN')
db.session.add(m)
m = CattleMovement(2,1,datetime.now(),'IN')
db.session.add(m)
m = CattleMovement(2,1,datetime.now(),'OUT')
db.session.add(m)
m = CattleMovement(3,2,datetime.now(),'IN')
db.session.add(m)
m = CattleMovement(2,2,datetime.now(),'IN')
db.session.add(m)
db.session.commit()

