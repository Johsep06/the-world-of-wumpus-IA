from src.agente import Agente

class AgenteReativo(Agente):
    def __init__(self, mundo):
        super().__init__(mundo)
        self.set_tipo()

    def __set_tipo(self):
        self._tipo = 2