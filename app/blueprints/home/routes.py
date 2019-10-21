from flask import render_template, url_for, send_from_directory, current_app
import os

from . import homeBlueprint


@homeBlueprint.route('/')
def index():

    return render_template('index.html')



@current_app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(current_app.root_path, 'static'),'favicon.ico', mimetype='image/vnd.microsoft.icon')
