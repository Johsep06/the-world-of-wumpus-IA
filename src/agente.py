from abc import ABC, abstractmethod

class Agente(ABC):
    def __init__(self):
        self._pontos = 0
        self.__registro = ''
        self._tipo = 0
        self.final = 0
        self.__historico_passos = ''
        self.qtd_passos = 0
        
    @abstractmethod
    def set_tipo(self): ...