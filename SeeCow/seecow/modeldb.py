# For running from commandline
# >>> python
# >>> exec(open("./seecow/modeldb.py").read())
# Preserves local variables!!

# initialize context & db
from seecow import create_app
app = create_app()
app.app_context().push()
from seecow import db
import seecow.model

from seecow.model import User
from seecow.model import Cattle
from seecow.model import Parlor
from seecow.model import CattleMovement

