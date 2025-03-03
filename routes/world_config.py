from flask import Blueprint, render_template

world_config_route = Blueprint('world-config', __name__)

@world_config_route.route('/')
def world_config(): 
    return render_template('world-config.html')