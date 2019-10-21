from flask import Blueprint, current_app


homeBlueprint = Blueprint('home', __name__, template_folder=current_app.config['TEMPLATE_FOLDER'], static_folder=current_app.config['STATIC_FOLDER'])
#homeBlueprint = Blueprint('home', __name__)


from . import routes

