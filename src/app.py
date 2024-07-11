from src.ambiente import Ambiente
from src.agente import Agente
from src.agente_aleatorio import AgenteAleatorio

__board: Ambiente
__ia:AgenteAleatorio

def novo_jogo(size: int):
    global __board
    pocos = int(size * size * (3/16))

    __board = None
    __board = Ambiente(size, pocos)

def seletor_agente(tipo:int):
    '''
    [ 1 ] - Agente Aleatório.
    '''
    global __board
    global __ia

    if tipo == 1:
        __ia = AgenteAleatorio(__board)
        
def acao():
    global __ia 
    __ia.agir()

def board():
    __board.set_out(True)
    return __board.getMap()

def map():
    global __board
    return __board.get_percepcoes()

def size():
    global __board
    return len(__board)

def get_relatorio():
    global __ia
    status = __ia.get_status()
    status['bag'] = __ia.get_bag()
    status['flecha'] = __ia.get_flechas()
    return status