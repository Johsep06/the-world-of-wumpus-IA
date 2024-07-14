from peewee import *

db = SqliteDatabase('database/jogos.db')

class Jogo(Model):
    n_passos = IntegerField()
    status_partida = CharField()
    historico = TextField()
    status_wumpus = CharField()
    pts = IntegerField()
    tamanho_mapa = IntegerField()
    tipo_agente = IntegerField()
    bag = CharField()
    flechas = IntegerField()

    class Meta:
        database = db