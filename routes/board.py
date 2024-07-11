from flask import Blueprint, render_template
from src.agente import Agente
from src.ambiente import Ambiente
from src.agente_aleatorio import AgenteAleatorio
from src.app import *

board_route = Blueprint('board', __name__)

@board_route.route('/')
def create_board():
    novo_jogo(4)
    seletor_agente(1)

    return render_template('board.html', 
                           board=board(), 
                           map=map(),
                           size=size()
                        )

@board_route.route('/update')
def update_board():
    acao()
    return render_template('board.html', 
                           board=board(), 
                           map=map(),
                           size=size()
                        )

@board_route.route('/status')
def status():
    status = get_relatorio()
    return render_template('statistics.html', 
                           pts=status['pts'],
                           passos=status['n_passos'],
                           percepcao=status['percepcao'],
                           flecha=status['flecha'],
                           bag=len(status['bag'])
                           )