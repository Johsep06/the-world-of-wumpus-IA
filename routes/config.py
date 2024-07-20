from flask import Blueprint, render_template, request, jsonify
from database.database import db, Jogo
from src.dados import serializar

db.connect()
db.create_tables([Jogo])

config_route = Blueprint('config', __name__)

@config_route.route('/')
def config():
    ag1_jogos = len(Jogo.select().where(Jogo.tipo_agente == 1))
    ag1_vit = len(Jogo.select().where(Jogo.tipo_agente == 1, Jogo.status_partida == 'v'))

    ag2_jogos = len(Jogo.select().where(Jogo.tipo_agente == 2))
    ag2_vit = len(Jogo.select().where(Jogo.tipo_agente == 2, Jogo.status_partida == 'v'))
    
    return render_template('config.html', 
                           ag1Qtd=ag1_jogos, Ag1Vit=ag1_vit,
                           ag2Qtd=ag2_jogos, Ag2Vit=ag2_vit)

@config_route.route('/set-agente', methods=['POST'])
def set_agente():
    try:
        data = request.get_json()
        agente_id = data.get('value')
        serializar(agente_id ,'./database/agente.bin')
        
        return jsonify({'success': True}), 200
    except Exception as e:
        print('Erro: ' + str(e))
        serializar(1, './database/agente.bin')
        return jsonify({'error': str(e)}), 500