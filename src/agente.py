from src.ambiente import Ambiente

class Agente(object):
    __pos = {'x':0, 'y':0}
    __bag = []
    __pts = 0
    __flecha = 1
    __status = {'n_passos':0, 'status_partida':'n', 'percepcao':'', 'historico':'', 'wumpus':'v'}

    def __init__(self, board: Ambiente, tipo_agente:int=0) -> None:
        self.__board = board
        self.__board.setAgente(self.__pos['x'], self.__pos['y'])
        self.__status['tamanho_do_mapa'] = len(board)
        self.__status['tipo_agente'] = tipo_agente
    
    def getPts(self) -> int:
        return self.__pts
    
    def get_flechas(self) -> int:
        return self.__flecha
    
    def get_bag(self): return self.__bag
    
    def get_pos(self) -> list[int]:
        return [self.__pos['y'], self.__pos['x']]
    
    def get_status(self) -> dict[str,any]:
        '''
        n_passos: int.
        status_partida [n:normal, v:vitoria, w:Wumpus, p:poço ].
        percepcao: str.
        historico: historido de acoes
        wumpus: [v: vivo, m: morto]
        pts: int
        tamanho_do_mapa: int
        tipo_agente: [0:jogador, 1:aleatório, 2:memoria, 3:aprendizado]
        bag: str
        flechas: int
        '''
        self.__status['pts'] = self.__pts
        # self['flechas'] = self.__flecha
        # self['bag'] = ''.join(self.__bag)
        return self.__status
    
    def __mover(self, direcao:str) -> int:
        '''Retorna
        \n-1 - Falha na operação
        \n0 - Nada acontece
        \n1 - Vitória
        \n2 - Devorado pelo Wumpus
        \n3 - Caiu no Poço
        \n4 - Movomento inválido
        '''

        status_aux = {0:'n', 1:'v', 2:'w', 3:'p'}

        if direcao == 'N':
            if self.__pos['y'] == 0: return 4
            self.__pos['y'] -= 1

        elif direcao == 'S':
            if self.__pos['y'] == len(self.__board) - 1: return 4
            self.__pos['y'] += 1
            
        elif direcao == 'L':
            if self.__pos['x'] == len(self.__board) - 1: return 4
            self.__pos['x'] += 1

        elif direcao == 'O':
            if self.__pos['x'] == 0: return 4
            self.__pos['x'] -= 1
            
        status_operacao, resultado = self.__board.changeAgente(self.__pos['x'], self.__pos['y'], self.__bag)

        if not status_operacao: return -1

        self.__pts -= 1
        self.__status['n_passos'] += 1
        self.__status['percepcao'] = self.__board.get_percepcao(self.__pos['x'], self.__pos['y'])

        if resultado == 1: self.__pts += 1_000
        elif resultado == 2 or resultado == 3: self.__pts -= 1_000

        self.__status['status_partida'] = status_aux[resultado]
        return resultado
    
    def __pegar(self) -> bool:
        tem_ouro = self.__board.getGold()

        if tem_ouro:
            self.__bag.append('G')
        
        return tem_ouro

    def __atirar(self, direcao: str) -> int:

        '''
        Retorna 0 para sem flechas.\n
        Retorna 1 para direção inválida.\n
        Retorna 2 para ação sem efeito.\n
        Retorna 3 para Wumpus morto.
        '''

        result = bool()
        
        if self.__flecha == 0: 
            return 0

        if direcao == 'n':
            if self.__pos['y'] == 0: return 1
            
            self.__flecha -= 1
            result = self.__board.killWumpus(self.__pos['x'], self.__pos['y'] - 1)
                

        elif direcao == 's':
            if self.__pos['y'] == len(self.__board) - 1: return 1

            self.__flecha -= 1
            result = self.__board.killWumpus(self.__pos['x'], self.__pos['y'] + 1) 

        elif direcao == 'l':
            if self.__pos['x'] == len(self.__board) - 1: return 1

            self.__flecha -= 1
            result = self.__board.killWumpus(self.__pos['x'] + 1, self.__pos['y'])

        elif direcao == 'o': 
            if self.__pos['x'] == 0: return 1

            self.__flecha -= 1
            result = self.__board.killWumpus(self.__pos['x'] - 1, self.__pos['y'])

        self.__pts -= 10
        if result: 
            self.__status['wumpus'] = 'm'
            return 3
        else:
            return 2

    def acao(self, acao:str) -> bool:
        '''
        Movimento: [N, S, L, O].
        Flecha: [n, s, l, o].
        pegar: x
        '''
        concluido = False

        if acao in ['N', 'S', 'L', 'O']:
            self.__mover(acao)
            concluido = True
        elif acao in ['n', 's', 'l', 'o']:
            self.__atirar(acao)
            concluido = True
        elif acao == 'x':
            self.__pegar()
            concluido = True

        if concluido:
            self.__status['historico'] += acao
        
        return concluido
        
    def get_acoes(self) -> dict[str,list[str]]:
        moves = {'M':[]}

        if self.__pos['y'] != 0: moves['M'].append('N')
        if self.__pos['y'] != len(self.__board): moves['M'].append('S')
        if self.__pos['x'] != len(self.__board): moves['M'].append('L')
        if self.__pos['x'] != 0: moves['M'].append('O')

        if 'f' in self.__board.get_percepcao(self.__pos['x'], self.__pos['y']) and self.__flecha != 0:
            moves['F'] = []
            if self.__pos['y'] != 0: moves['F'].append('n')
            if self.__pos['y'] != len(self.__board): moves['F'].append('s')
            if self.__pos['x'] != len(self.__board): moves['F'].append('l')
            if self.__pos['x'] != 0: moves['F'].append('o')
            
        if 'b' in self.__board.get_percepcao(self.__pos['x'], self.__pos['y']) and self.__board.getGold(pegar=False):
            moves['P'] = ['x']

        return moves