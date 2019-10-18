import click
from flask.cli import with_appcontext

from app.models import db
# from .models import User, Question

from flask import current_app

@click.command(name='create_tables')
@with_appcontext
def create_tables():
    print('current_app.config["SQLALCHEMY_DATABASE_URI"] = ', current_app.config['SQLALCHEMY_DATABASE_URI'])
    db.create_all()
