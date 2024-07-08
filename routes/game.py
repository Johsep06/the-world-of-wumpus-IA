from flask import Blueprint, render_template

game_route = Blueprint('game', __name__)

size = 4

@game_route.route('/')
def home():
    return render_template('game.html', size=size)