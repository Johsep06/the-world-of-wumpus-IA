import random

from sala import Sala

class Ambiente:
    def __init__(self, size:int, wumpus_qtd:int=1, poco_qtd:int=3, gold_qtd:int=1):
        '''
        Objeto Ambiente será responsável guardar e processar os dados do mundo de wumpus.
        - size:int = Tamanho do mundo, o mundo sempre será de tamanho quadrado.
        - wumpus_qtd:int é a quantidade de Wumpus no mundo.
        - poco_qtd:int = é a quantidade de Poços no mundo.
        - gold_qtd:int = é a quantidade de Ouro no mundo.
        '''
        
        # Criação do mundo aplicado o objeto 'Sala' para cada posição.
        self.__mundo = [
            [Sala() for i in range(size) ] for i in range(size)
        ]
        
        self.__posicoes = {
            'O':[],
            'W':[],
            'P':[]
        }

        # Salva o tamanho do mundo no objeto.
        self.__size = size 
        
        for i in range(size - 1): 
            # Define a posição aleatória do objeto Poço.
            pos = self.__set_object('P', 'b')
            self.__posicoes['P'].append(pos) 

        for i in range(wumpus_qtd): 
            # Define a posição aleatória do objeto Wumpus.
            self.__set_object('W', 'f') 
            self.__posicoes['W'].append(pos) 

        for i in range(gold_qtd): 
            # Define a posição aleatória do objeto Ouro.
            self.__set_gold() 
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
    
    def __to_dict(self) -> dict: 
        dado = {
            
        }
    
    def get_word(self) -> list[Sala]:
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

            if not e_posicao_inicial and sala_sem_poco:
                self.__mundo[pos_i][pos_j].objeto = 'O' # seta objeto 'O' para representar o ouro.
                self.__mundo[pos_i][pos_j].percepcao = 'br' # senta a percepção br para representar o brilho

                return pos_i, pos_j 

    def __set_object(self, objeto:str, percepcao:str) -> tuple[int, int]:
        '''
        Função que cálcula a posição aleatória do ouro e sua percepção.
        '''
        while True:
            pos_i = random.randint(0, self.__size - 1)
            pos_j = random.randint(0, self.__size - 1)
            
            # verifica se as posição cálculada é a inicial
            e_posicao_inicial = pos_i == 0 and pos_j == 0

            # verifica se as posição cálculada está sem Poço
            sala_sem_poco = self.__mundo[pos_i][pos_j].objeto != 'P'

            if not e_posicao_inicial and sala_sem_poco:
                # Salva o objeto na sala
                self.__mundo[pos_i][pos_j].objeto = objeto
                
                # cálcula se existe a posição abaixo da cálculada
                if pos_i + 1 < self.__size:
                    if percepcao not in self.__mundo[pos_i + 1][pos_j].percepcao:
                        self.__mundo[pos_i + 1][pos_j].percepcao = percepcao
                    
                # cálcula se existe a posição a direita da cálculada
                if pos_j + 1 < self.__size: 
                    if percepcao not in self.__mundo[pos_i][pos_j + 1].percepcao:
                        self.__mundo[pos_i][pos_j + 1].percepcao = percepcao
                    
                # cálcula se existe a posição acima da cálculada
                if pos_i - 1 >= 0:
                    if percepcao not in self.__mundo[pos_i - 1][pos_j].percepcao:
                        self.__mundo[pos_i - 1][pos_j].percepcao = percepcao
                    
                # cálcula se existe a posição a esquerda da cálculada
                if pos_j - 1 >= 0:
                    if percepcao not in self.__mundo[pos_i][pos_j - 1].percepcao:
                        self.__mundo[pos_i][pos_j - 1].percepcao = percepcao
                
                return pos_i, pos_j

if __name__ == '__main__': 
    # funçao de testes do objeto
    mapa = Ambiente(20)
    # print((mapa.get_word()))
    print(mapa)
    print()
    print(mapa.show_percepcoes())