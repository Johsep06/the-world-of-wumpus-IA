import random

from src.sala import Sala
from database.database import get_mundo_qtd

class Ambiente:
    def __init__(self):
        '''
        Objeto Ambiente será responsável guardar e processar os dados do mundo de wumpus.
        '''
        self.__mundo:list[list[Sala]] = None
        self.__id:int = None
        self.__size:int = None
        self.__posicoes = {}

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
    
    def new(self, size:int, wumpus_qtd:int=None, poco_qtd:int=None, gold_qtd:int=None):
        '''
        Cria um novo mundo apagando o antigo.
        - size:int = Tamanho do mundo, o mundo sempre será de tamanho quadrado.
        - wumpus_qtd:int é a quantidade de Wumpus no mundo.
        - poco_qtd:int = é a quantidade de Poços no mundo.
        - gold_qtd:int = é a quantidade de Ouro no mundo.
        '''
        
        # Salva o tamanho do mundo na classe.
        self.__size = size
        
        # Define o id do objeto
        self.__id = get_mundo_qtd()
        
        # Criação do mundo aplicado o objeto 'Sala' para cada posição.
        self.__mundo = [
            [Sala() for j in range(self.__size) ] for i in range(self.__size)
        ]
        
        self.__mundo[0][0].objeto = 'S'
        
        if poco_qtd is None:
            poco_qtd = self.__size - 1
            
        if gold_qtd is None:
            gold_qtd = int(self.__size / 6)
            
            if gold_qtd == 0:
                gold_qtd = 1
        
        if wumpus_qtd is None:
            wumpus_qtd = int(self.__size / 5)
            
            if wumpus_qtd == 0:
                wumpus_qtd = 1
            
        self.__posicoes = {
            'O':[],
            'W':[],
            'P':[]
        }
        
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
        '''
        Função que desfaz as alterações feitas por um agente no mundo.
        '''
        
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
            'id': self.__id
        }
        
        return dado

    def salas_dict(self) -> list[dict]:
        dados:list[dict] = []
        
        for i in range(self.__size):
            for j in range(self.__size):
                sala = self.__mundo[i][j].to_dict()
                sala['mundo_id'] = self.__id
                sala['pos_i'] = i
                sala['pos_j'] = j
                dados.append(sala)

        return dados
                   
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
