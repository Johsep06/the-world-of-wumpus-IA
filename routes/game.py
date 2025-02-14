from flask import Blueprint, render_template

from src.ambiente import Ambiente
from src.sala import Sala

game_route = Blueprint('game', __name__)

mundo = Ambiente()

@game_route.route('/')
def game(): 
    return render_template('game.html')

@game_route.route('/world')
def render_world():
    mundo.new(25)
    return render_template('board.html', size=len(mundo), world=mundo.get_word())