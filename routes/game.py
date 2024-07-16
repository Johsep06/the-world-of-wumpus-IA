from flask import Blueprint, render_template, request
from src.app import Game

game_route = Blueprint('game', __name__)

size = 4
jogo = Game()
jogo.new_game(4,1)

@game_route.route('/')
def home():
    return render_template('game.html', size=size)

@game_route.route('/set-size', methods=['POST'])
def set_size():
    global size
    
    data = request.get_json()
    size = int(data.get('value'))
    

@game_route.route('/load-board')
def load_board():
    jogo.new_game(size, 1)

    
    return render_template('board.html', 
                           board=jogo.tabuleiro(), 
                           map=jogo.get_percepcoes(),
                           size=len(jogo)
                        )

@game_route.route('/update-board')
def update_board():
    jogo.jogada()

    return render_template('board.html', 
                           board=jogo.tabuleiro(), 
                           map=jogo.get_percepcoes(),
                           size=len(jogo)
                        )

@game_route.route('/status')
def get_status():
    status = jogo.get_relatorio()

    return render_template('statistics.html',
                           pts=status['pts'],
                           passos=status['n_passos'],
                           percepcao=status['percepcao'],
                           flecha=status['flecha'],
                           bag=len(status['bag']),
                           status=status['status_partida']
                           )