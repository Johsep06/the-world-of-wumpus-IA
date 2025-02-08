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
        self.__agents = {}

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
                if self.__mundo[pos_i][pos_j].objeto == '-':
                    self.__mundo[pos_i][pos_j].objeto = 'O' 
                else:
                    self.__mundo[pos_i][pos_j].objeto += 'O' 

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
                if self.__mundo[pos_i][pos_j].objeto == '-':
                    self.__mundo[pos_i][pos_j].objeto = objeto
                else:
                    self.__mundo[pos_i][pos_j].objeto += objeto
                
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
        self.__id = 15#get_mundo_qtd()
        
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
    
    def load(self, size:int, id:int, salas:tuple[tuple]):
        self.__size = size
        self.__id = id
        
        self.__posicoes = {
            'O':[],
            'W':[],
            'P':[]
        }
        
        self.__mundo = [
            [
                None for _ in range(size)
            ] for _ in range(size)
        ]
        for dado in salas:
            i = dado[1]
            j = dado[2]

            sala = Sala()
            sala.percepcao = dado[3]
            sala.objeto = dado[4]
            
            if 'O' in sala.objeto:
                self.__posicoes['O'].append((i, j))
            if 'W' in sala.objeto:
                self.__posicoes['W'].append((i, j))
            if 'P' in sala.objeto:
                self.__posicoes['P'].append((i, j))
            
            self.__mundo[i][j] = sala
    
    def reload(self):
        '''
        Função que desfaz as alterações feitas por um agente no mundo.
        '''
        
        for key in self.__posicoes:
            for i,j in self.__posicoes[key]:
                if key.upper() not in str(self.__mundo[i][j]):
                    self.__mundo[i][j].objeto = self.__mundo[i][j].objeto.upper()
    
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
                   
    def get_word(self) -> list[list[str]]:
        '''
        Retorna a matriz de objetos mundo
        '''
        saida = []
        for i in range(self.__size):
            saida.append([])
            for j in range(self.__size):
                objeto = self.__mundo[i][j].objeto
                saida[i].append(objeto)
                
        return saida

    def get_percepcoes(self) -> list[list[str]]:
        '''
        Retorna a matriz de objetos mundo
        '''
        saida = []
        for i in range(self.__size):
            saida.append([])
            for j in range(self.__size):
                percepcao = self.__mundo[i][j].percepcao
                saida[i].append(percepcao)
                
        return saida

    def check_status(self, agente_id:int):
        '''
        Retorna o status atual do mundo com base na sala atual
        '''
        status = ''
        
        pos_i = self.__agents[agente_id]['pos_i']
        pos_j = self.__agents[agente_id]['pos_j']
        
        # Verifica se o agente foi devorado pelo wumpus
        devorado = 'W' in self.__mundo[pos_i][pos_j].objeto
        
        # Verifica se o agente caiu no poço
        caiu = 'P' in self.__mundo[pos_i][pos_j].objeto
        
        if devorado:
            status = 'W'
        elif caiu:
            status = 'P'
        else:
            status = '-'
        
        saida = {
            'percepcao':self.__mundo[pos_i][pos_j].percepcao,
            'status':status
        }
        
        
        return saida
    
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

    def set_agente(self, agente_id:int, pos_i:int=None, pos_j:int=None):
        if pos_i is None:
            pos_i = 0

        if pos_j is None:
            pos_j = 0
            
        self.__agents[agente_id] = { 'pos_i':pos_i, 'pos_j':pos_j}
        self.__mundo[pos_i][pos_j].caminho = 'A'
        
    def mover(self, agente_id:int, direcao:str):
        direcoes = {
            'N':(-1, 0),
            'S':(1, 0),
            'L':(0, 1),
            'O':(0, -1),
        }
        
        pos_i = self.__agents[agente_id]['pos_i']
        pos_j = self.__agents[agente_id]['pos_j']

        self.__mundo[pos_i][pos_j].caminho = '-'
        pos_i += direcoes[direcao][0]
        pos_j += direcoes[direcao][1]
        self.__mundo[pos_i][pos_j].caminho = 'A'
        self.__agents[agente_id]['pos_i'] = pos_i
        self.__agents[agente_id]['pos_j'] = pos_j
    
    def atirar(self, agente_id:int, direcao:str, flechas:int):
        if flechas == 0: return ''

        direcoes = {
            'n':(-1, 0),
            's':(1, 0),
            'l':(0, 1),
            'o':(0, -1),
        }
        
        pos_i = self.__agents[agente_id]['pos_i']
        pos_j = self.__agents[agente_id]['pos_j']
        pos_i += direcoes[direcao][0]
        pos_j += direcoes[direcao][1]

        if 'W' in self.__mundo[pos_i][pos_j].objeto:
            objeto = self.__mundo[pos_i][pos_j].objeto.replace('W', 'w')
            self.__mundo[pos_i][pos_j].objeto = objeto
    
    def pegar(self, agente_id:int):
        pos_i = self.__agents[agente_id]['pos_i']
        pos_j = self.__agents[agente_id]['pos_j']
        
        if 'O' in self.__mundo[pos_i][pos_j].objeto:
            objeto = self.__mundo[pos_i][pos_j].objeto.replace('O', 'o')
            self.__mundo[pos_i][pos_j].objeto = objeto

            return 'O'

        else:
            return ''
        
    def direcoes_possiveis(self, agente_id:int):
        pos_i = self.__agents[agente_id]['pos_i']
        pos_j = self.__agents[agente_id]['pos_j']

        saida = ''
        
        if pos_i != 0:
            saida += 'N'
        if pos_i != self.__size - 1:
            saida += 'S'
        if pos_j != 0:
            saida += 'O'
        if pos_j != self.__size - 1:
            saida += 'L'

        return saida