from flask import Blueprint, render_template
from src.main import *

board_route = Blueprint('board', __name__)

# __board = [
#     ['A','', '', 'P'],
#     ['','', 'P', ''],
#     ['','', '', 'P'],
#     ['','W', '', 'G']
# ]

__board = tabu.getMap()
print(__board)
__map = [
    ['','', 'v', ''],
    ['','v', '', 'v'],
    ['','f', 'v', ''],
    ['f','', 'f', 'b']
]

__agente = [0, 0]

size = 4

@board_route.route('/')
def create_board():
    return render_template('board.html', board=__board, size=size, map=__map, agente=__agente)