from flask import Blueprint, render_template
from src.app import Game

board_route = Blueprint('board', __name__)

jogo = Game()

@board_route.route('/')
def create_board():
    jogo.new_game(4, 1)

    return render_template('board.html', 
                           board=jogo.tabuleiro(), 
                           map=jogo.get_percepcoes(),
                           size=len(jogo)
                        )

@board_route.route('/update')
def update_board():
    jogo.jogada()

    return render_template('board.html', 
                           board=jogo.tabuleiro(), 
                           map=jogo.get_percepcoes(),
                           size=len(jogo)
                        )

@board_route.route('/status')
def status():
    status = jogo.get_relatorio()

    return render_template('statistics.html',
                           pts=status['pts'],
                           passos=status['n_passos'],
                           percepcao=status['percepcao'],
                           flecha=status['flecha'],
                           bag=len(status['bag']),
                           status=status['percepcao']
                           )