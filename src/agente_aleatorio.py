from src.agente import Agente
import random

class AgenteAleatorio(Agente):
    def __init__(self, mundo):
        super().__init__(mundo)
        print(self.id)
        self.__ja_atirou = False
    
    def set_tipo(self):
        self._tipo = 1
        
    def __decidir(self):
        dados_sala = self._mundo.check_status(self.id, self.inventario)
        direcoes = self._mundo.direcoes_possiveis(self.id)
        choice = random.choice(direcoes)
        
        flecha = self.inventario['flecha']
        
        if 'br' in dados_sala['percepcao']:
            self._mundo.pegar(self.id)
            self.inventario['ouro'] += 1
        if 'f' in dados_sala['percepcao'] and flecha > 0 and not self.__ja_atirou:
            self._mundo.atirar(self.id, choice.lower())
            self.inventario['flecha'] -= 1
            self.__ja_atirou = True
        else:
            self.__ja_atirou = False
            self._mundo.mover(self.id, choice)
        
        # if 'br' in dados_sala['percepcao']:
        #     choice = 'x'
        # elif 'f' in dados_sala['percepcao'] and flecha > 0:
        #     self.inventario['flecha'] -= 1
        #     choice = choice.lower()
            
    
    def agir(self):
        self.__decidir()
            
        