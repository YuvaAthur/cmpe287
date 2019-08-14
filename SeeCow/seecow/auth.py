import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

from flask_login import LoginManager, current_user, login_user, logout_user
# from flask.ext.login import LoginManager
login_manager = LoginManager()


# from werkzeug.security import check_password_hash, generate_password_hash

# from seecow.dbconn import get_db
from seecow.model import User

bp = Blueprint('auth', __name__, url_prefix='/auth')


from flask_login import login_required


@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get(int(user_id))

#check for validity of user
@login_manager.user_loader
def load_user(userid):
    return User.query.get(int(user_id))


@bp.route('/register', methods=('GET', 'POST'))
def register():
    """Register a new user.
    Validates that the username is not already taken. Hashes the
    password for security.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif User.query.filter_by(username=username).first() is not None:
            error = 'User {0} is already registered.'.format(username)
            flash(error)
            return redirect(url_for('auth.login')) # adding redirect in case registered


        if error is None:
            # the name is available, store it in the database and go to
            # the login page
            u = User(username,password)
            u.save()
            return redirect(url_for('auth.login'))

        flash(error)

    return render_template('auth/register.html')


@bp.route('/login', methods=('GET', 'POST'))
def login():
    """Log in a registered user by adding the user id to the session."""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        user = User.query.filter_by(username=username).first()

        if user is None:
            error = 'Incorrect username.'
        elif not user.check_password(password):
            error = 'Incorrect password.'
        
        if error is None:
            # store the user id in a new session and return to the index
            session.clear()
            session['user_id'] = user.id   
          

        # Security features
        # Ref: https://riptutorial.com/flask/example/28112/using-flask-login-extension
            # Login and validate the user.
            # user should be an instance of your `User` class
            login_user(user)
            # flash('User is active? {0}'.format(user_.is_active))
            # flash('User is authenticated? {0}'.format(current_user.is_authenticated))

        #  securing redirect URL using flask login mechanimsms
            # flash('Logged in successfully.')

            next = request.args.get('next')
            # is_safe_url should check if the url is safe for redirects.
            # See http://flask.pocoo.org/snippets/62/ for an example.
            if not is_safe_url(next):
                return abort(400)

            return redirect(next or url_for('index'))

        flash(error)

    return render_template('auth/login.html')


@bp.route('/logout')
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    logout_user()
    return redirect(url_for('index'))


#Not availanle here: https://flask-login.readthedocs.io/en/latest/#login-example
#Ref: From Wayback machine - snippets
#http://flask.pocoo.org/snippets/62/

# try:
#     from urllib.parse import urlparse, urljoin
# except ImportError:
#      from urlparse import urlparse, urljoin

from urllib.parse import urlparse, urljoin
from flask import request, url_for

def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and \
           ref_url.netloc == test_url.netloc

def get_redirect_target():
    for target in request.values.get('next'), request.referrer:
        if not target:
            continue
        if is_safe_url(target):
            return target

def redirect_back(endpoint, **values):
    target = request.form['next']
    if not target or not is_safe_url(target):
        target = url_for(endpoint, **values)
    return redirect(target)
