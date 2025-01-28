class Celula:
    def __init__(self):
        '''
        Célula que será usada para facilitar o armazenamento dos dados do "Mundo de Wumpus" sendo.
            - objeto:str = objeto presente na casa (Wumpus, Poço, ou Ouro).
            - percepcao:str = percepção que afeta a casa (fedor, brisa e brilho).
            - caminho:str= parte da célula por onde o agente vai se mover sem sobreescrever os outos dados.
        '''
        self.__objeto = ''
        self.__percepcao = ''
        self.__caminho = ''
        self.__exibir = '-'
    
    @property
    def exibir(self) -> str:
        '''
        Função responsável por exibir o dado de "maior prioridade" da céclula (Caminho > Objeto)
        '''
        if self.__caminho != '':
            self.__exibir = self.__caminho
        else:
            self.__exibir = self.__objeto
        
        return self.__exibir
    
    @property
    def objeto(self) -> str:
        return self.__objeto
    
    @objeto.setter
    def objeto(self, value: str):
        self.__objeto = value
    
    @property
    def caminho(self) -> str:
        return self.__caminho
    
    @caminho.setter
    def caminho(self, value: str):
        self.__caminho = value
        
    @property
    def percepcao(self) -> str:
        return self.__percepcao
    
    @percepcao.setter
    def percepcao(self, value:str):
        self.__percepcao = value

    def __str__(self) -> str:
        return self.exibir
    
if __name__ == '__main__':
    cell = Celula()
    cell.objeto = 'W'
    # cell.caminho = 'A'
    print(cell.exibir)