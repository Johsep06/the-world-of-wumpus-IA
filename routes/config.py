from flask import Blueprint, render_template, request
from database.database import db, Jogo

db.connect()
db.create_tables([Jogo])




config_route = Blueprint('config', __name__)

@config_route.route('/')
def config():
    total_jogos = len(Jogo.select())
    vitorias = len(Jogo.select().where(Jogo.status_partida == 'v'))
    
    return render_template('config.html', qtd=total_jogos, vit=vitorias)

@config_route.route('/', methods=['POST'])
def parametros_game(): 
    data = request.json
    pass