from time import sleep
from src.agente import Agente
from src.ambiente import Ambiente
from src.agente_aleatorio import AgenteAleatorio
from src.agente_reativo_2 import AgenteReativo2
from src.memory import Memory
from src.app import Game

def seletor_agente(tipo:int, board:Ambiente):
    '''
    [ 1 ] - Agente Aleatório.
    [ 2 ] - Agente Reativo 2.
    '''

    agente = None
    if tipo == 1:
        agente = AgenteAleatorio(board)
    elif tipo == 2:
        agente = AgenteReativo2(board)
        
    return agente

def novo_jogo(size: int):
    pocos = int(size * size * (3/16))

    board = Ambiente(size, pocos)
    return board

board = novo_jogo(5)
board.set_out(True)
ia = seletor_agente(2, board)
print(board)
sleep(1)

try:
    while True:
        ia.agir()
        print('\n\n')
        print(board)
        status = ia.get_status()['status_partida']
        sleep(1)
        if status in ['v', 'w', 'p']:
            break
except:
    pass

finally:
    print('\n')
    s = ia.get_status()
    for k in list(s.keys()): print(k, s[k], sep=': ')
    print('bag :',ia.get_bag())