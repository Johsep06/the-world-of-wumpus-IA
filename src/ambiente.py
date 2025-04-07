import random

from src.sala import Sala
from database.database import get_mundo_qtd
from datetime import datetime

class Ambiente:
    def __init__(self):
        '''
        Objeto Ambiente será responsável guardar e processar os dados do mundo de wumpus.
        '''
        self.__mundo:dict[tuple,Sala] = None
        self.__id:int = None
        self.__size:int = None
        self.__posicoes = {}
        self.__agents:dict[str, tuple] = {}

    @property
    def id(self):
        return self.__id

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
            posicao = random.choice(list(self.__mundo.keys()))
            
            # verifica se as posição cálculada é a inicial
            e_posicao_inicial = posicao == (0, 0, 0)

            # verifica se as posição cálculada está sem Poço
            sala_sem_poco = self.__mundo[posicao].objeto != 'P'
            
            objeto_repetido = 'O' not in self.__mundo[posicao].objeto

            if not e_posicao_inicial and sala_sem_poco and objeto_repetido:
                # seta objeto 'O' para representar o ouro.
                if self.__mundo[posicao].objeto == '-':
                    self.__mundo[posicao].objeto = 'O' 
                else:
                    self.__mundo[posicao].objeto += 'O' 

                # seta a percepção br para representar o brilho
                percepcao_na_sala = self.__mundo[posicao].percepcao
                if percepcao_na_sala == '-':
                    self.__mundo[posicao].percepcao = 'br' 
                else:
                    self.__mundo[posicao].percepcao += 'br' 

                return posicao
    
    def __set_object(self, objeto:str, percepcao:str) -> tuple[int, int]:
        '''
        Função que cálcula a posição aleatória do ouro e sua percepção.
        '''
        while True:
            posicao = random.choice(list(self.__mundo.keys()))
            
            # verifica se as posição cálculada é a inicial
            e_posicao_inicial = posicao == (0, 0, 0)

            # verifica se as posição cálculada está sem Poço
            sala_sem_poco = self.__mundo[posicao].objeto != 'P'
            
            objeto_repetido = objeto not in self.__mundo[posicao].objeto

            if not e_posicao_inicial and sala_sem_poco and objeto_repetido:
                # Salva o objeto na sala
                if self.__mundo[posicao].objeto == '-':
                    self.__mundo[posicao].objeto = objeto
                else:
                    self.__mundo[posicao].objeto += objeto
            
                for direcao in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    posicao_proxima = posicao[0] + direcao[0], posicao[1] + direcao[1], 0
                    if posicao_proxima in self.__mundo:
                        if percepcao not in self.__mundo[posicao_proxima].percepcao:
                            percepcao_na_sala = self.__mundo[posicao_proxima].percepcao
                            if percepcao_na_sala == '-':
                                self.__mundo[posicao_proxima].percepcao = percepcao
                            else:
                                self.__mundo[posicao_proxima].percepcao = ',' + percepcao
                
                return posicao
            
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
        self.__id = datetime.now()
        
        # Criação do mundo aplicado o objeto 'Sala' para cada posição.
        self.__mundo = {}
        for i in range(self.__size):
            for j in range(self.__size):
                self.__mundo[(i, j, 0)] = Sala()
        
        self.__mundo[(0,0,0)].objeto = 'S'
        
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
        
        self.__mundo = {}

        for dado in salas:
            posicao = dado[1], dado[2], dado[3]

            sala = Sala()
            sala.percepcao = dado[4]
            sala.objeto = dado[5]
            
            if 'O' in sala.objeto:
                self.__posicoes['O'].append(posicao)
            if 'W' in sala.objeto:
                self.__posicoes['W'].append(posicao)
            if 'P' in sala.objeto:
                self.__posicoes['P'].append(posicao)
            
            self.__mundo[posicao] = sala
    
    def reload(self):
        '''
        Função que desfaz as alterações feitas por um agente no mundo.
        '''
        
        for key in self.__posicoes:
            for posicao in self.__posicoes[key]:
                if key.upper() not in str(self.__mundo[posicao]):
                    self.__mundo[posicao].objeto = self.__mundo[posicao].objeto.upper()
                    self.__mundo[posicao].percepcao = self.__mundo[posicao].percepcao.lower()
    
    def to_dict(self) -> dict:
        '''
        Retorna o mundo em forma de dicionario
        '''
        dados = {
            'size': self.__size,
            'id': self.__id
        }
        
        return dados

    def salas_dict(self) -> list[dict]:
        dados:list[dict] = []

        for posicao in self.__mundo:
            sala = self.__mundo[posicao].to_dict()
            sala['mundo_id'] = self.__id
            sala['pos_x'] = posicao[0]
            sala['pos_y'] = posicao[1]
            sala['pos_z'] = posicao[2]
            dados.append(sala)

        return dados
                   
    def get_word(self) -> list[dict[tuple, str]]:
        '''
        Retorna a matriz de objetos mundo
        '''
        saida = []
        for posicao in self.__mundo:
            saida.append({
                posicao:self.__mundo[posicao].objeto
            })
                
        return saida

    def get_percepcoes(self) -> list[dict[tuple, str]]:
        '''
        Retorna a matriz de objetos mundo
        '''
        saida = []
        for posicao in self.__mundo:
            saida.append({
                posicao:self.__mundo[posicao].percepcao
            })
                
        return saida

    def get_relatorio(self) -> dict:
        relatorio = {
            'O':len(self.__posicoes['O']),
            'W':len(self.__posicoes['W']),
            'P':len(self.__posicoes['P']),
        }
        
        return relatorio

    def check_status(self, agente_id:int, inventario:dict[str,int]):
        '''
        Retorna o status atual do mundo com base na sala atual.
        keys: percepcao, status
        '''
        status = ''
        
        posicao = self.__agents[agente_id]
        
        # Verifica se o agente foi devorado pelo wumpus
        devorado = 'W' in self.__mundo[posicao].objeto
        
        # Verifica se o agente caiu no poço
        caiu = 'P' in self.__mundo[posicao].objeto
        
        vitoria = False

        if posicao == (0, 0, 0):
            if inventario['ouro'] > 0:
                vitoria = True
        
        if devorado:
            status = 'W'
        elif caiu:
            status = 'P'
        elif vitoria:
            status = 'V'
        else:
            status = '-'
        
        saida = {
            'percepcao':self.__mundo[posicao].percepcao,
            'status':status
        }
        
        return saida
    
    def show_world(self) -> str:
        ''' 
        Função que exibe o estado do mundo pela prioridade da sala.
        '''
        saida = ''
        linha = (min(self.__mundo, key=lambda x: x[0])[0], max(self.__mundo, key=lambda x: x[0])[0])
        coluna = (min(self.__mundo, key=lambda x: x[1])[1], max(self.__mundo, key=lambda x: x[1])[1])
        profundidade = (min(self.__mundo, key=lambda x: x[2])[2], max(self.__mundo, key=lambda x: x[2])[2])

        for p in range(profundidade[0], profundidade[1] + 1):
            for l in range(linha[0], linha[1] + 1):
                for c in range(coluna[0], coluna[1] + 1):
                    if (l, c, p) in self.__mundo:
                        saida += f' | {str(self.__mundo[(l, c, p)]): ^3}'
                    else:
                        saida += ' |    '
                saida += ' |\n'
            saida += '\n'
        
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

    def set_agente(self, agente_id:int, pos_x:int=None, pos_y:int=None, pos_z:int = None):
        if pos_x is None:
            pos_x = 0

        if pos_y is None:
            pos_y = 0

        if pos_z is None:
            pos_z = 0
            
        posicao = (pos_x, pos_y, pos_z)
        
        self.__agents[agente_id] = posicao
        self.__mundo[posicao].caminho = 'A'
        
    def mover(self, agente_id:int, direcao:str):
        direcoes = {
            'N':(-1, 0, 0),
            'S':(1, 0, 0),
            'O':(0, -1, 0),
            'L':(0, 1, 0),
            'C':(0, 0, -1),
            'B':(0, 0, 1),
        }
        
        posicao = self.__agents[agente_id]
        destino = (
            direcoes[direcao][0] + posicao[0],
            direcoes[direcao][1] + posicao[1],
            direcoes[direcao][2] + posicao[2],
        )


        self.__mundo[posicao].caminho = '-'
        self.__mundo[destino].caminho = 'A'
        self.__agents[agente_id] = destino
    
    def atirar(self, agente_id:int, direcao:str):
        direcoes = {
            'n':(-1, 0, 0),
            's':(1, 0, 0),
            'o':(0, -1, 0),
            'l':(0, 1, 0),
            'c':(0, 0, -1),
            'b':(0, 0, 1),
        }
        
        posicao = self.__agents[agente_id]
        alvo = (
            direcoes[direcao][0] + posicao[0],
            direcoes[direcao][1] + posicao[1],
            direcoes[direcao][2] + posicao[2],
        )
        
        if 'W' in self.__mundo[alvo].objeto:
            objeto = self.__mundo[alvo].objeto.replace('W', 'w')
            self.__mundo[alvo].objeto = objeto
            return 'g'
    
    def pegar(self, agente_id:int):
        posicao = self.__agents[agente_id]
        
        if 'O' in self.__mundo[posicao].objeto:
            objeto = self.__mundo[posicao].objeto.replace('O', 'o')
            percepcao = self.__mundo[posicao].percepcao.replace('br', 'BR')
            self.__mundo[posicao].objeto = objeto
            self.__mundo[posicao].percepcao = percepcao

            return 'O'
        else:
            return ''
        
    def direcoes_possiveis(self, agente_id:int):
        posicao = self.__agents[agente_id]

        saida = ''
        
        direcoes = {
            (-1, 0, 0):'N',
            (1, 0, 0):'S',
            (0, -1, 0):'O',
            (0, 1, 0):'L',
            (0, 0, -1):'C',
            (0, 0, 1):'B',
        }
        
        for x,y,z in direcoes:
            nova_posicao = (posicao[0] + x, posicao[1] + y, posicao[2] + z)

            if nova_posicao in self.__mundo:
                saida += direcoes[(x, y, z)]

        return saida
    
    def get_coordenada(self, agente_id):
        posicao = self.__agents[agente_id]
        
        return posicao

    def get_indices(self):
        posicoes = list(self.__mundo.keys())

        x_menor = min(posicoes, key=lambda x: x[0])[0]
        y_menor = min(posicoes, key=lambda x: x[1])[1]
        z_menor = min(posicoes, key=lambda x: x[2])[2]

        x_maior = max(posicoes, key=lambda x: x[0])[0]        
        y_maior = max(posicoes, key=lambda x: x[0])[1]        
        z_maior = max(posicoes, key=lambda x: x[0])[2]
        
        indices = [
            (x_menor, x_maior),
            (y_menor, y_maior),
            (y_menor, z_maior),
        ]

        return indices
    
    def checar_posicao(self, posicao:tuple):
        
        if posicao not in self.__mundo:
            return 'F'
        
        return self.__mundo[posicao].objeto