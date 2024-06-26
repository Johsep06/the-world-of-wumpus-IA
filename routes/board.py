from flask import Blueprint, render_template
from src.main import *

board_route = Blueprint('board', __name__)

# __board = [
#     ['A','', '', 'P'],
#     ['','', 'P', ''],
#     ['','', '', 'P'],
#     ['','W', '', 'G']
# ]
board.set_out(True)
__tabu = board.getMap()
__map = board.get_percepcoes()

__agente = [0, 0]

size = len(board)

@board_route.route('/')
def create_board():
    return render_template('board.html', board=__tabu, size=size, map=__map, agente=__agente)