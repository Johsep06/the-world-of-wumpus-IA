from flask import Blueprint, render_template, request, jsonify
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
                           size=len(jogo),
                        )

@game_route.route('/relatorio')
def get_relatorio():
    relatorio = jogo.get_relatorio()

    return render_template('statistics.html',
                           pts=relatorio['pts'],
                           passos=relatorio['n_passos'],
                           percepcao=relatorio['percepcao'],
                           flecha=relatorio['flecha'],
                           bag=len(relatorio['bag']),
                           status=relatorio['status_partida']
                           )

@game_route.route('/status-game', methods=['GET'])
def get_status():
    status = jogo.get_relatorio()['status_partida']
    return jsonify(status=status)

# @game_route.route('/teste', methods=['GET'])
# def teste():
#     status = jogo.get_relatorio()
#     return jsonify(status)