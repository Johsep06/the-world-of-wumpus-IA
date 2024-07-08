from src.ambiente import Ambiente
from src.agente import Agente
from src.agente_aleatorio import AgenteAleatorio

def seletor_agente(tipo:int, board:Ambiente):
    '''
    [ 1 ] - Agente Aleatório.
    '''

    agente = None
    if tipo == 1:
        agente = AgenteAleatorio(board)
        
    return agente


board: Ambiente
ia:AgenteAleatorio = seletor_agente(1)