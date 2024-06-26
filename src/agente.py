from src.ambiente import Ambiente

class Agente(object):
    __pos = {'x':0, 'y':0}
    __bag = []
    __pts = 0
    __flecha = 1

    def __init__(self, board: Ambiente) -> None:
        self.__board = board
        self.__board.setAgente(self.__pos['x'], self.__pos['y'])
    
    def getPts(self) -> int:
        return self.__pts
    
    def __mover(self, direcao:str) -> int:
        '''Retorna
        \n-1 - Falha na operação
        \n0 - Nada acontece
        \n1 - Vitória
        \n2 - Devorado pelo Wumpus
        \n3 - Caiu no Poço
        \n4 - Movomento inválido
        '''

        if direcao == 'N':
            if self.__pos['y'] == 0: return 4
            self.__pos['y'] -= 1
            self.__pts -= 1

        elif direcao == 'S':
            if self.__pos['y'] == len(self.__board) - 1: return 4
            self.__pos['y'] += 1
            self.__pts -= 1
            
        elif direcao == 'L':
            if self.__pos['x'] == len(self.__board) - 1: return 4
            self.__pos['x'] += 1
            self.__pts -= 1

        elif direcao == 'O':
            if self.__pos['x'] == 0: return 4
            self.__pos['x'] -= 1
            self.__pts -= 1
            
        status_operacao, resultado = self.__board.changeAgente(self.__pos['x'], self.__pos['y'], self.__bag)

        if not status_operacao: return -1

        if resultado == 1: self.__pts += 1_000
        elif resultado == 2 or resultado == 3: self.__pts -= 1_000

        return resultado
    
    def __pegar(self) -> bool:
        tem_ouro = self.__board.getGold()

        if tem_ouro:
            self.__bag = 'G'
        
        return tem_ouro

    def __atirar(self, direcao: str) -> int:

        '''
        Retorna 0 para sem flechas.\n
        Retorna 1 para direção inválida.\n
        Retorna 2 para ação sem efeito.\n
        Retorna 3 para Wumpus morto.
        '''

        result = bool()
        
        if self.__flecha == 0: return 0

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
        if result: return 3
        else: return 2

    def acao(self, acao:str) -> int:
        '''
        Movimento: [N, S, L, O].
        Flecha: [n, s, l, o].
        pegar: x
        '''

        if acao in ['N', 'S', 'L', 'O']:
            self.__mover(acao)
        elif acao in ['n', 's', 'l', 'o']:
            self.__atirar(acao)
        elif acao == 'x':
            self.__pegar()
        
    def get_acoes(self) -> dict[str,list]:
        acoes = {'M':[]}

        if self.__pos['y'] != 0: acoes['M'].append('N')
        if self.__pos['y'] != len(self.__board): acoes['M'].append('S')
        if self.__pos['x'] != len(self.__board): acoes['M'].append('L')
        if self.__pos['x'] != 0: acoes['M'].append('O')

        if self.__board.get_percepcao(self.__pos['x'], self.__pos['y']) == 'f':
            acoes['F'] = []
            if self.__pos['y'] != 0: acoes['F'].append('N')
            if self.__pos['y'] != len(self.__board): acoes['F'].append('S')
            if self.__pos['x'] != len(self.__board): acoes['F'].append('L')
            if self.__pos['x'] != 0: acoes['F'].append('O')
            
        if self.__board.get_percepcao(self.__pos['x'], self.__pos['y']) == 'B':
            acoes['P'] = ['x']
            pass

        return acoes