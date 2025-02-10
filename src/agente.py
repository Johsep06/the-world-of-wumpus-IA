from abc import ABC, abstractmethod
from datetime import datetime

from src.ambiente import Ambiente
from src.sala import Sala
from database import database

class Agente(ABC):
    def __init__(self, mundo:Ambiente):
        self._id = database.get_agente_qtd()
        self._mundo = mundo
        self._mundo.set_agente(self.id)
        self._pontos = 0
        self.__registro = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self._tipo = 0
        self.final = {}
        self._historico_passos = ''
        self.inventario = {
            'flecha': mundo.get_relatorio()['W'],
            'ouro': 0
        }
        self._wumpus = 0;
        
    @property
    def id(self):
        return self._id
      
    @abstractmethod
    def set_tipo(self): ...
    
    def to_dict(self):
        dados = {
            'id': self.id,
            'pontos':self._pontos,
            'flechas':self.inventario['flecha'],
            'registro':self.__registro,
            'tipo':self._tipo,
            'final':self.final['status'],
            'historico_passos':self._historico_passos,
            'qtd_passos':len(self._historico_passos),
            'wumpus':self._wumpus,
            'mundo_id':self._mundo.id,
        }
        
        return dados
    
    def status(self):
        game = self._mundo.check_status(self.id, self.inventario)
        self.final = game

        return game['status']