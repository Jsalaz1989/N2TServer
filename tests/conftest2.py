import pytest
from app.models import User
from flask_security.utils import hash_password
from app import create_app

from app.config import TestingConfig

@pytest.fixture(scope='module')
def test_client():
    flask_app = create_app(TestingConfig)
 
    # Flask provides a way to test your application by exposing the Werkzeug test Client
    # and handling the context locals for you.
    testing_client = flask_app.test_client()
 
    # Establish an application context before running the tests.
    ctx = flask_app.app_context()
    ctx.push()
 
    yield testing_client  # this is where the testing happens!
 
    ctx.pop()
 
@pytest.fixture(scope='module')
def new_user():
    user = User(email='guest@fake.com', password=hash_password('test123'))
    return user

@pytest.fixture(scope='module')
def new_potential_user():
    user = User(email='guest@fake.com', password=hash_password('test123'))
    return user