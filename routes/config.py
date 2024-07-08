from flask import Blueprint, render_template

config_route = Blueprint('config', __name__)

@config_route.route('/')
def config(): 
    return render_template('config.html')

@config_route.route('/', methods=['POST'])
def parametros_game(): 
    pass