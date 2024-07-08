from flask import Blueprint, render_template
from src.agente import Agente
from src.ambiente import Ambiente
from src.agente_aleatorio import AgenteAleatorio

board_route = Blueprint('board', __name__)

board = Ambiente(4, 3)
ia = AgenteAleatorio(board)

@board_route.route('/')
def create_board():
    board.set_out(True)

    return render_template('board.html', 
                           board=board.getMap(), 
                           map=board.get_percepcoes(), 
                           size=len(board)
                        )
