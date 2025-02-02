import random

from sala import Sala

class Ambiente:
    def __init__(self, size:int, wumpus_qtd:int=None, poco_qtd:int=None, gold_qtd:int=None):
        '''
        Objeto Ambiente será responsável guardar e processar os dados do mundo de wumpus.
        - size:int = Tamanho do mundo, o mundo sempre será de tamanho quadrado.
        - wumpus_qtd:int é a quantidade de Wumpus no mundo.
        - poco_qtd:int = é a quantidade de Poços no mundo.
        - gold_qtd:int = é a quantidade de Ouro no mundo.
        '''
        
        # Criação do mundo aplicado o objeto 'Sala' para cada posição.
        self.__mundo = [
            [Sala() for j in range(size) ] for i in range(size)
        ]
        
        self.__mundo[0][0].objeto = 'S'
        
        if poco_qtd is None:
            poco_qtd = size - 1
            
        if gold_qtd is None:
            gold_qtd = int(size / 6)
            
            if gold_qtd == 0:
                gold_qtd = 1
        
        if wumpus_qtd is None:
            wumpus_qtd = int(size / 5)
            
            if wumpus_qtd == 0:
                wumpus_qtd = 1
            
        self.__posicoes = {
            'O':[],
            'W':[],
            'P':[]
        }

        # Salva o tamanho do mundo no objeto.
        self.__size = size 
        
        # Define o id do objeto
        self._id = None
        
        for i in range(poco_qtd): 
            # Define a posição aleatória do objeto Poço.
            pos = self.__set_object('P', 'b')
            self.__posicoes['P'].append(pos) 

        for i in range(wumpus_qtd): 
            # Define a posição aleatória do objeto Wumpus.
            pos = self.__set_object('W', 'f') 
            self.__posicoes['W'].append(pos) 

        for i in range(gold_qtd): 
            # Define a posição aleatória do objeto Ouro.
            pos = self.__set_gold() 
            self.__posicoes['O'].append(pos) 

        
    def __str__(self): 
        '''
        Função que permite a converção do objeto em string.
        '''
        return self.show_world()
    
    def __len__(self): 
        '''
        Função que permite a a leitua do tamanho do mundo pela a função len.
        '''
        return self.__size
    
    def __set_gold(self) -> tuple[int, int]:
        '''
        Função que cálcula a posição aleatória do ouro e sua percepção.
        '''
        while True:
            pos_i = random.randint(0, self.__size - 1) # cálcula a posição i
            pos_j = random.randint(0, self.__size - 1)# cálcula a posição j

            # verifica se as posição cálculada é a inicial
            e_posicao_inicial = pos_i == 0 and pos_j == 0

            # verifica se as posição cálculada está sem Poço
            sala_sem_poco = 'P' not in self.__mundo[pos_i][pos_j].objeto

            objeto_repetido = 'O' not in self.__mundo[pos_i][pos_j].objeto

            if not e_posicao_inicial and sala_sem_poco and objeto_repetido:
                # seta objeto 'O' para representar o ouro.
                self.__mundo[pos_i][pos_j].objeto = 'O' 

                # senta a percepção br para representar o brilho
                self.__mundo[pos_i][pos_j].percepcao = 'br' 

                return pos_i, pos_j 

    def __set_object(self, objeto:str, percepcao:str) -> tuple[int, int]:
        '''
        Função que cálcula a posição aleatória do ouro e sua percepção.
        '''
        while True:
            pos_i = random.randint(0, self.__size - 1) # cálcula a posição i
            pos_j = random.randint(0, self.__size - 1) # cálcula a posição j
            
            # verifica se as posição cálculada é a inicial
            e_posicao_inicial = pos_i == 0 and pos_j == 0

            # verifica se as posição cálculada está sem Poço
            sala_sem_poco = self.__mundo[pos_i][pos_j].objeto != 'P'
            
            objeto_repetido = objeto not in self.__mundo[pos_i][pos_j].objeto

            if not e_posicao_inicial and sala_sem_poco and objeto_repetido:
                # Salva o objeto na sala
                self.__mundo[pos_i][pos_j].objeto = objeto
                
                # cálcula se existe a posição abaixo da cálculada e seta a percepção
                if pos_i + 1 < self.__size:
                    if percepcao not in self.__mundo[pos_i + 1][pos_j].percepcao:
                        self.__mundo[pos_i + 1][pos_j].percepcao = percepcao
                    
                # cálcula se existe a posição a direita da cálculada e seta a percepção
                if pos_j + 1 < self.__size: 
                    if percepcao not in self.__mundo[pos_i][pos_j + 1].percepcao:
                        self.__mundo[pos_i][pos_j + 1].percepcao = percepcao
                    
                # cálcula se existe a posição acima da cálculada e seta a percepção
                if pos_i - 1 >= 0:
                    if percepcao not in self.__mundo[pos_i - 1][pos_j].percepcao:
                        self.__mundo[pos_i - 1][pos_j].percepcao = percepcao
                    
                # cálcula se existe a posição a esquerda da cálculada e seta a percepção
                if pos_j - 1 >= 0:
                    if percepcao not in self.__mundo[pos_i][pos_j - 1].percepcao:
                        self.__mundo[pos_i][pos_j - 1].percepcao = percepcao
                
                return pos_i, pos_j
    
    def reload(self):
        for key in self.__posicoes:
            for i,j in self.__posicoes[key]:
                if key not in str(self.__mundo[i][j]):
                    self.__mundo[i][j] = key

    def to_dict(self) -> dict:
        '''
        Retorna o mundo em forma de dicionario
        '''
        dado = {
            'size': self.__size,
            'posicoes': self.__posicoes
        }
    
    def get_word(self) -> list[Sala]:
        '''
        Retorna a matriz do mundo
        '''
        return self.__mundo
    
    def show_world(self) -> str:
        ''' 
        Função que exibe o estado do mundo pela prioridade da sala.
        '''
        saida = ''

        for linha in self.__mundo:
            for valor in linha:
                saida += f' | {str(valor): ^3}'
            saida += ' |\n'

        return saida
    
    def show_percepcoes(self) -> str:
        ''' 
        Função que exibe asm percepções do mundo.
        '''
        saida = ''

        for linha in self.__mundo:
            for valor in linha:
                saida += f' | {valor.percepcao: ^3}'
            saida += ' |\n'

        return saida

    def get_percepcao(self, pos_i:int, pos_j:int):
        '''
        Retorna a percepçao de uma sala específica
        '''
        return self.__mundo[pos_i][pos_j].percepcao

if __name__ == '__main__': 
    # funçao de testes do objeto
    mapa = Ambiente(5)
    print(mapa)
    print(mapa.reload())
    print(mapa)