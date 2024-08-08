from flask import Blueprint, render_template
from database.database import db, Jogo

# db.connect()
db.create_tables([Jogo])

result_route = Blueprint('result', __name__)

@result_route.route('/')
def resultados():
    return render_template('result.html')

@result_route.route('/table')
def render_table():
    agente_1 = [[], [], [], [], []]
    agente_2 = [[], [], [], [], []]

#todo   Mapa 20X20
#todo   Mapa 4x4
    aux = Jogo.select().where(Jogo.tipo_agente == 1, Jogo.tamanho_mapa == 4)
    for i in range(-1, -21, -1):
        try:
            agente_1[0].append(aux[i].pts)
        except:
            agente_1[0].append(0)

    aux = Jogo.select().where(Jogo.tipo_agente == 2, Jogo.tamanho_mapa == 4)
    for i in range(-1, -21, -1):
        try:
            agente_2[0].append(aux[i].pts)
        except:
            agente_2[0].append(0)


#todo   Mapa 5x5
    aux = Jogo.select().where(Jogo.tipo_agente == 1, Jogo.tamanho_mapa == 5)
    for i in range(-1, -21, -1):
        try:
            agente_1[1].append(aux[i].pts)
        except:
            agente_1[1].append(0)

    aux = Jogo.select().where(Jogo.tipo_agente == 2, Jogo.tamanho_mapa == 5)
    for i in range(-1, -21, -1):
        try:
            agente_2[1].append(aux[i].pts)
        except:
            agente_2[1].append(0)


#todo   Mapa 10X10
    aux = Jogo.select().where(Jogo.tipo_agente == 1, Jogo.tamanho_mapa == 10)
    for i in range(-1, -21, -1):
        try:
            agente_1[2].append(aux[i].pts)
        except:
            agente_1[2].append(0)

    aux = Jogo.select().where(Jogo.tipo_agente == 2, Jogo.tamanho_mapa == 10)
    for i in range(-1, -21, -1):
        try:
            agente_2[2].append(aux[i].pts)
        except:
            agente_2[2].append(0)


#todo   Mapa 15x15
    aux = Jogo.select().where(Jogo.tipo_agente == 1, Jogo.tamanho_mapa == 15)
    for i in range(-1, -21, -1):
        try:
            agente_1[3].append(aux[i].pts)
        except:
            agente_1[3].append(0)

    aux = Jogo.select().where(Jogo.tipo_agente == 2, Jogo.tamanho_mapa == 15)
    for i in range(-1, -21, -1):
        try:
            agente_2[3].append(aux[i].pts)
        except:
            agente_2[3].append(0)

            
#todo   Mapa 20x20
    aux = Jogo.select().where(Jogo.tipo_agente == 1, Jogo.tamanho_mapa == 20)
    for i in range(-1, -21, -1):
        try:
            agente_1[4].append(aux[i].pts)
        except:
            agente_1[4].append(0)

    aux = Jogo.select().where(Jogo.tipo_agente == 2, Jogo.tamanho_mapa == 20)
    for i in range(-1, -21, -1):
        try:
            agente_2[4].append(aux[i].pts)
        except:
            agente_2[4].append(0)
        
    return render_template('tables-lines.html', agente1=agente_1, agente2=agente_2)