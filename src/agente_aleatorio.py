from src.agente import Agente
import random

class AgenteAleatorio(Agente):
    def __init__(self, mundo):
        super().__init__(mundo)
        self.__ja_atirou = False
        self.set_tipo()
    
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
            som = self._mundo.atirar(self.id, choice.lower())
            self.inventario['flecha'] -= 1
            self.__ja_atirou = True

            self._pontos -= 10
            if som == 'g':
                self._wumpus += 1
                self._pontos += 1000
        else:
            self.__ja_atirou = False
            self._mundo.mover(self.id, choice)
            self._historico_passos += choice
            self._pontos -= 1
            
        self.status()
            
        if self.final['status'] == 'V':
            self._pontos += 1000 * self.inventario['ouro']
        elif self.final['status'] == 'W':
            self._pontos -= 1000
        elif self.final['status'] == 'P':
            self._pontos -= 1000

    
    def agir(self):
        self.__decidir()
            
        