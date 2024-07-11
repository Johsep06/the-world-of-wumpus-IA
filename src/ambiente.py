from random import randrange
from src.celula import Celula

class Ambiente(object):
    def __init__(self, size: int, qtd_pocos: int, qtd_wumpus:int=1, qtd_gold:int=1) -> None:
        self.__size = size
        self.__posX = 0
        self.__posY = 0

        self.__board = [[Celula('') for j in range(size)] for i in range(size)]
        self.__board[self.__posY][self.__posX].setObjeto('S')

        for i in range(qtd_gold): self.__setGold()
        for i in range(qtd_wumpus): self.__setObjeto('W', 'f')
        for i in range(qtd_pocos): self.__setObjeto('P', 'v')

    def __str__(self) -> str:
        out = ''
        for i in self.__board:
            aux = []
            for j in i: aux.append(j.getOut())
            out += ' | '.join(aux)
            out += '\n'

        percp = self.__board[self.__posY][self.__posX].getPercepcao()
        out += f'\nPercepção: {percp}'
        return out
    
    def __len__(self) -> int:
        return self.__size
    
    def __setGold(self):
        i,j = 0,0
        while True:
            i = randrange(0, self.__size)
            j = randrange(0, self.__size)

            if i == 0 and j == 0: continue
            if self.__board[i][j].getObjeto() != '': continue
            
            break

        self.__board[i][j].setObjeto('G')
        self.__board[i][j].setPercepcao('b')

    def __setObjeto(self, simblo: str, percepcao: str):
        i,j = 0,0
        while True:
            i = randrange(0, self.__size)
            j = randrange(0, self.__size)

            if i == 0 and j == 0: continue
            if self.__board[i][j].getObjeto() != '': continue
            
            break

        self.__board[i][j].setObjeto(simblo)
        
        if i != 0:
            self.__board[i - 1][j].setPercepcao(percepcao)
        
        if i != self.__size - 1:
            self.__board[i + 1][j].setPercepcao(percepcao)

        if j != 0:
            self.__board[i][j - 1].setPercepcao(percepcao)
        
        if j != self.__size - 1:
            self.__board[i][j + 1].setPercepcao(percepcao)

    def set_out(self, exibir: bool):
        if exibir:
            for i in range(self.__size):
                for j in range(self.__size):
                    if self.__board[i][j].getValue() == 'A':
                        if self.__board[i][j].getObjeto() in ['O', '']:
                            self.__board[i][j].setOut(0)
                        else:
                            self.__board[i][j].setOut(1)

                    else: self.__board[i][j].setOut(1)
                            
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    self.__board[i][j].setOut(0)

    def get_board(self) -> list[list[str]]:
        tabuleiro = []
        for linha in self.__board:
            aux = []
            for celula in linha:
                if celula.getValue() == 'A':
                    aux.append(celula.getValue())
                else:
                    aux.append(celula.getOut())
            tabuleiro.append(aux.copy())
        return tabuleiro


    def setAgente(self, posX: int, posY: int):
        self.__board[posY][posX].setValue('A')
        self.__board[posY][posX].setOut(0)

    def changeAgente(self, posX:int, posY:int, bag: list) -> tuple[bool, int]:
        '''
        \n(-1) - Movomento inválido
        \n0 - Nada acontece
        \n1 - Vitória
        \n2 - Devorado pelo Wumpus
        \n3 - Caiu no Poço
        '''
        try:
            self.__board[self.__posY][self.__posX].setValue('')
            self.__board[self.__posY][self.__posX].setOut(1)
            self.__board[posY][posX].setValue('A')
            self.__board[posY][posX].setOut(0)
            self.__posX = posX
            self.__posY = posY

            if self.__board[posY][posX].getObjeto() == 'W':
                return True, 2

            if self.__board[posY][posX].getObjeto() == 'P':
                return True, 3
            
            if posX == 0 and posY == 0 and 'G' in bag:
                return True, 1
            else: return True, 0
        except:
            return False, -1

    def getGold(self, pegar=True) -> bool:
        if self.__board[self.__posY][self.__posX].getObjeto() == 'G' and pegar:
            self.__board[self.__posY][self.__posX].setObjeto('')
            self.__board[self.__posY][self.__posX].setPercepcao('')
            return True
        
        elif not pegar and self.__board[self.__posY][self.__posX].getObjeto() == 'G':
            return True

        else: return False

    def killWumpus(self, posX:int, posY:int) -> bool:
        if self.__board[posY][posX].getObjeto() == 'W':
            self.__board[posY][posX].setObjeto('')
            return True
        else: return False

    def getMap(self) -> list[list[str]]:
        tabu = []
        for t in self.__board:
            aux = []
            for c in t:
                aux.append(str(c.getOut()))
            tabu.append(aux.copy())
        return tabu

    def get_percepcoes(self) -> list[list[str]]:
        tabu = []
        for t in self.__board:
            aux = []
            for c in t:
                aux.append(str(c.getPercepcao()))
            tabu.append(aux.copy())
        return tabu
    
    def get_percepcao(self, pos_x: int, pos_y: int) -> str:
        return self.__board[pos_y][pos_x].getPercepcao()