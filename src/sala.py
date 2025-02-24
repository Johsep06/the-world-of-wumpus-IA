class Sala:
    def __init__(self):
        '''
        Sala que será usada para facilitar o armazenamento dos dados do "Mundo de Wumpus" sendo.
            - objeto:str = objeto presente na casa (Wumpus, Poço, ou Ouro).
            - percepcao:str = percepção que afeta a casa (fedor, brisa e brilho).
            - caminho:str = parte da Sala por onde o agente vai se mover sem sobreescrever os outos dados.
        '''
        self.__objeto = '-'
        self.__percepcao = ['-']
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
            self.__objeto = value
    
    @property
    def caminho(self) -> str:
        return self.__caminho
    
    @caminho.setter
    def caminho(self, value: str):
        self.__caminho = value

    @property
    def percepcao(self) -> str:
        return ','.join( self.__percepcao)
    
    @percepcao.setter
    def percepcao(self, value:str):
        if value not in self.__percepcao and '-' in self.percepcao:
            self.__percepcao[0] = value
        elif value not in self.__percepcao:
            self.__percepcao.append(value)

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