import click
from flask.cli import with_appcontext

from app.models import db
# from .models import User, Question

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    print('app.config["SQLALCHEMY_DATABASE_URI"] = ', app.config['SQLALCHEMY_DATABASE_URI'])
    db.create_all()
