from ambiente import Ambiente
from celula import Celula

class Agente(object):
    __pos = {'x':0, 'y':0}
    __bag = []
    __pts = 0

    def __init__(self, board: Ambiente) -> None:
        self.__board = board
        self.__board.setAgente(self.__pos['x'], self.__pos['y'])

    def getDirecao(self) -> str:
        return self.__skin
    
    def getPts(self) -> int:
        return self.__pts
    
    def mover(self, direcao:str) -> int:
        '''
        Retorna
        \n0 para neutro 
        \n1 para fim de jogo
        \n2 para movimento inválido
        \n3 para vitória
        '''
        pass
    
    def seguir(self) -> int:
        '''
        Retorna
        \n0 para neutro 
        \n1 para fim de jogo
        \n2 para movimento inválido
        \n3 para vitória
        '''

        resultado = -1
        gameOver = -1
        if self.__sentido == 'n':
            if self.__posY == 0: return 2
            self.__posY -= 1
            gameOver, resultado = self.__board.changeAgente(self.__skin, self.__posX, self.__posY, self.__bag)

        elif self.__sentido == 's':
            if self.__posY == self.__board.shape(1): return 2
            self.__posY += 1
            gameOver, resultado = self.__board.changeAgente(self.__skin, self.__posX, self.__posY, self.__bag)

        elif self.__sentido == 'l':
            if self.__posX == self.__board.shape(2): return 2
            self.__posX += 1
            gameOver, resultado = self.__board.changeAgente(self.__skin, self.__posX, self.__posY, self.__bag)

        elif self.__sentido == 'o':
            if self.__posX == 0: return 2
            self.__posX -= 1
            gameOver, resultado = self.__board.changeAgente(self.__skin, self.__posX, self.__posY, self.__bag)

        if self.__posX == 0 and self.__posY == 0 and gameOver:
            if resultado == 1: self.__pts += 1_000
            else: self.__pts -= 1_000
            return 3
        return int(gameOver)
    
    def pegar(self):
        temOuro = self.__board.getGold()

        if temOuro:
            self.__bag = 'G'

    def atirar(self) -> int:

        '''
        Retorna 0 para sem flechas.\n
        Retorna 1 para direção inválida.\n
        Retorna 2 para ação sem efeito.\n
        Retorna 3 para Wumpus morto.
        '''

        result = bool()
        
        if self.__flecha == 0: return 0

        if self.__sentido == 'n':
            if self.__posY == 0: return 1
            
            self.__flecha -= 1
            result = self.__board.killWumpus(self.__posX, self.__posY - 1)
                

        elif self.__sentido == 's':
            if self.__posY == self.__board.shape(1) + 1: return 1

            self.__flecha -= 1
            result = self.__board.killWumpus(self.__posX, self.__posY + 1) 

        elif self.__sentido == 'l':
            if self.__posX == self.__board.shape(2) + 1: return 1

            self.__flecha -= 1
            result = self.__board.killWumpus(self.__posX + 1, self.__posY)

        elif self.__sentido == 'o': 
            if self.__posX == 0: return 1

            self.__flecha -= 1
            result = self.__board.killWumpus(self.__posX - 1, self.__posY)

        self.__pts -= 10
        if result: return 3
        else: return 2
            