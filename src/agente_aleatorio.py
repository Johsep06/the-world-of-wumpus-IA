from src.agente import Agente
from src.ambiente import Ambiente
from random import choice

class AgenteAleatorio(Agente):
    def __init__(self, board: Ambiente) -> None:
        super().__init__(board)

    def agir(self):
        moves = super().get_acoes()
        
        keys = list(moves.keys())
        decisao = ''

        if 'P' in keys:
            decisao = choice(moves['P'])
        elif 'F' in keys:
            decisao = choice(moves['F'])
        else: 
            decisao = choice(moves['M'])

        self.acao(decisao)
