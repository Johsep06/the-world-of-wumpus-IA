from flask import Blueprint, jsonify

from database import database
from src.ambiente import Ambiente

db_route = Blueprint('db', __name__)

@db_route.route('/')
def db(): 
    dados = database.get_all_worlds()
    mundo = Ambiente()
    return