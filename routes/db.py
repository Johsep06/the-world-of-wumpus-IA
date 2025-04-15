from flask import Blueprint, jsonify

from database import database
from src.ambiente import Ambiente

db_route = Blueprint('db', __name__)

@db_route.route('/')
def db(): 
    dados = database.get_all_worlds()
    mundos = []
    for dado in dados:
        mundo = Ambiente()
        mundo.load(**dado)
        mundos.append({
            'id':dado['id'],
            'indices':mundo.get_indices(),
            'salas':mundo.mundo_formatado(),
        })
    return jsonify(mundos)