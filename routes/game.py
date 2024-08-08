from flask import Blueprint, render_template, request, jsonify
from src.app import Game, save_game
from src.dados import desserializar

game_route = Blueprint('game', __name__)

def get_agente():
    try:
        return int(desserializar('./database/agente.bin'))
    except Exception as e:
        print('erro na seleção de agentes\n' + e)
        return 1

agente_id = get_agente()

size = 4
jogo = Game()
jogo.new_game(4,agente_id)

@game_route.route('/')
def home():
    return render_template('game.html', size=size)

@game_route.route('/set-size', methods=['POST'])
def set_size():
    global size
    
    data = request.get_json()
    size = int(data.get('value'))
    return jsonify({'success': True}), 200

    

@game_route.route('/load-board')
def load_board():
    agente_id = get_agente()

    jogo.new_game(size, agente_id)

    
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
    relatorio = jogo.get_relatorio() 
    status = relatorio['status_partida']

    if status in ['v', 'w', 'p']:
        save_game(relatorio)

    return jsonify(status=status)

@game_route.route('/teste', methods=['GET'])
def teste():
    status = jogo.get_relatorio()
    return jsonify(status)