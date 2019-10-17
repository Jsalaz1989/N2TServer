from os import urandom, environ

class BaseConfig(object):
    """Base config class"""

    DEBUG = True
    TESTING = False

    EXPLAIN_TEMPLATE_LOADING = True

    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_SSL = True
    MAIL_USERNAME = 'autom8t8r@gmail.com'
    MAIL_PASSWORD = 'autom8t8r123'
    MAIL_DEBUG = True 
    MAIL_SUPPRESS_SEND = False
    MAIL_DEFAULT_SENDER = 'autom8t8r@gmail.com'

    SECRET_KEY = urandom(24)
    SECURITY_PASSWORD_SALT = 'penis'
    #SESSION_COOKIE_HTTPONLY = True     # True by default
    SECURITY_CONFIRMABLE = True
    #SECURITY_EMAIL_SENDER = 'autom8t8r@gmail.com'	# defaults to Flask-Mail's MAIL_DEFAULT_SENDER

    SQLALCHEMY_DATABASE_URI = 'postgresql://localhost/n2t'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # eventually will become unecessary

    # index = 'index.html'
    # SECURITY_FORGOT_PASSWORD_TEMPLATE = index	
    # SECURITY_LOGIN_USER_TEMPLATE = index
    # SECURITY_REGISTER_USER_TEMPLATE = index	
    # SECURITY_RESET_PASSWORD_TEMPLATE = index
    # SECURITY_CHANGE_PASSWORD_TEMPLATE = index
    # SECURITY_SEND_CONFIRMATION_TEMPLATE = index
    # SECURITY_SEND_LOGIN_TEMPLATE = index

    CORS_HEADERS = 'Content-Type'




class ProductionConfig(BaseConfig):
    """Production specific config"""
    
    DEBUG = False
    SESSION_COOKIE_SECURE = True    # requires https?

    TEMPLATE_FOLDER = 'N2TApp/client/build'
    STATIC_FOLDER = 'N2TApp/client/build/static'



class DevelopmentConfig(BaseConfig):
    """Development environment specific configuration"""
 
    DEBUG = True
    TESTING = True

    TEMPLATE_FOLDER = '../templates'
    STATIC_FOLDER = '../client/public'


class TestingConfig(BaseConfig):
    """Testing environment specific configuration"""
 
    # Bcrypt algorithm hashing rounds (reduced for testing purposes only!)
    BCRYPT_LOG_ROUNDS = 4
    
    # Enable the TESTING flag to disable the error catching during request handling
    # so that you get better error reports when performing test requests against the application.
    TESTING = True
    
    # Disable CSRF tokens in the Forms (only valid for testing purposes!)
    WTF_CSRF_ENABLED = False

    TEMPLATE_FOLDER = '../client/public'
    STATIC_FOLDER = '../client/public'


