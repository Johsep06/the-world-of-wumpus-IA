from src.agente import Agente
from src.ambiente import Ambiente
from random import choice

class AgenteAleatorio(Agente):
    def __init__(self, board: Ambiente) -> None:
        super().__init__(board)

    def agir(self):
        moves = super().get_acoes()
        
        keys = list(moves.keys())

        if 'P' in keys:
            self.acao(moves['P'][0])
        elif 'F' in keys:
            self.acao(choice(moves['F']))
        else: 
            self.acao(choice(moves['M']))
