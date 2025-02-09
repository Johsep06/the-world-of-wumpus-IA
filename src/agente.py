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
        self.final = 0
        self._historico_passos = ''
        self.qtd_passos = 0
        self.inventario = {
            'flecha': mundo.get_relatorio()['W'],
            'ouro': 0
        }
    @property
    def id(self):
        return self._id
      
    @abstractmethod
    def set_tipo(self): ...
    
    def to_dict(self): ...
    
    def status(self):
        game = self._mundo.check_status(self.id, self.inventario)

        return game['status']