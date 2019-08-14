import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# transitioning to SQLAlchemuy
db = SQLAlchemy()

def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY='dev',
        # store the database in the instance folder
        DATABASE=os.path.join(app.instance_path, 'seecow.sqlite'),
        # configuration for using dashboard templates
        # check by running
        CSRF_ENABLED = True,
        #SQLAlchemy is ORM for SQLite
        SQLALCHEMY_TRACK_MODIFICATIONS 	= False,
	    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(app.instance_path, 'seecow.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/hello')
    # @app.route('/')   # - For debugging purposes
    def hello():
        return 'Hello, World!'

    #return app

    # transitioning to SQLAlchemuy
    db.init_app(app)

    # # register the database commands
    # from seecow import model
    # model.init_app(app)



    # apply the blueprints to the app
    from seecow import camfeed,auth, dashboard
    app.register_blueprint(camfeed.bp)
    app.register_blueprint(auth.bp)
    app.register_blueprint(dashboard.bp)

    # make url_for('index') == url_for('camfeed.index')
    app.add_url_rule('/', endpoint='index')

    from flask_login import LoginManager
    # from flask.ext.login import LoginManager
    login_manager = LoginManager()
    login_manager.init_app(app) # app is a Flask object
    @login_manager.user_loader
    def load_user(user_id):
        return None
    
    return app
