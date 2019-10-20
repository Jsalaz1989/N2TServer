from flask import Flask, render_template
from .models import db, User, Role, migrate
from flask_security import Security, SQLAlchemyUserDatastore
from flask_cors import CORS




from os.path import abspath

from .email import mail

from .config import DevelopmentConfig, ProductionConfig

from app import commands

import traceback
import sys

import os


#Config = 'config.DevelopmentConfig'
#def create_app(config_class=Config):
def create_app(config_class=DevelopmentConfig):

    if os.environ.get('FLASK_ENV') == 'production':
        config_class = ProductionConfig

    # print('init.py : sys.last_traceback = ', sys.last_traceback)
    print('init.py : config_class = ', config_class)


    # Load Flask app    
    app = Flask(__name__, instance_path=abspath('.'), instance_relative_config=True)


    
    # Register the blueprints
    with app.app_context():
       
        # Load configuration
        #print('config_class = ', abspath(config_class))
        app.config.from_object(config_class)

        # Import blueprints (NOTE: needs to be here after app.config)
        from .blueprints.home import homeBlueprint
        from .blueprints.auth import authBlueprint

        app.register_blueprint(homeBlueprint)
        app.register_blueprint(authBlueprint)

        # Initialize database (Heroku doesn't see DATABASE_URL?)
        print('init.py : app.config["SQLALCHEMY_DATABASE_URI"] = ', app.config['SQLALCHEMY_DATABASE_URI'])
        db.init_app(app)

    # Catch-all chooses client routes (React) over server routes (Flask)
    @app.route('/', defaults={'path': ''})
    @app.route('/<path:path>')
    def catch_all(path):
        return render_template('index.html')
        #return 'You want path: %s' % path



    # Initialize database migration
    migrate.init_app(app, db)
    
    # Initialize mail service
    mail.init_app(app)
        
    # Setup Flask-Security
    userDatastore = SQLAlchemyUserDatastore(db, User, Role)
    security = Security(app, userDatastore)     # must be after loading everything into app, like registering blueprints
    CORS(app)

    app.cli.add_command(commands.create_tables)
    
    return app