class Sala:
    def __init__(self):
        '''
        Sala que será usada para facilitar o armazenamento dos dados do "Mundo de Wumpus" sendo.
            - objeto:str = objeto presente na casa (Wumpus, Poço, ou Ouro).
            - percepcao:str = percepção que afeta a casa (fedor, brisa e brilho).
            - caminho:str = parte da Sala por onde o agente vai se mover sem sobreescrever os outos dados.
        '''
        self.__objeto = '-'
        self.__percepcao = '-'
        self.__caminho = '-'
        self.__exibir = '-'
    
    @property
    def exibir(self) -> str:
        '''
        Função responsável por exibir o dado de "maior prioridade" da céclula (Caminho > Objeto)
        '''
        if self.__caminho != '-':
            self.__exibir = self.__caminho
        else:
            self.__exibir = self.__objeto
        
        return self.__exibir
    
    @property
    def objeto(self) -> str:
        return self.__objeto
    
    @objeto.setter
    def objeto(self, value: str):
        if self.__objeto == '-':
            self.__objeto = value
        else:
            self.__objeto += value
    
    @property
    def caminho(self) -> str:
        return self.__caminho
    
    @caminho.setter
    def caminho(self, value: str):
        return self.__caminho

    @property
    def percepcao(self) -> str:
        return self.__percepcao
    
    @percepcao.setter
    def percepcao(self, value:str):
        if self.__percepcao == '-':
            self.__percepcao = value
        else:
            self.__percepcao += ',' + value

    def __str__(self) -> str:
        return self.exibir
    
    def to_dict(self) -> dict:
        saida = {
            'percepcao': self.percepcao,
            'objeto': self.objeto
        }
        
        return saida
    
    def from_dict(self, sala:dict):
        self.__objeto = sala['objeto']
        self.__percepcao = sala['percpcao']
    
if __name__ == '__main__':
    '''
    Teste de Funcionamento do Objeto
    '''
    cell = Sala()
    cell.objeto = 'W'
    # cell.caminho = 'A'
    print(cell.exibir)