import random

from celula import Celula

class Ambiente:
    def __init__(self, size:int=4, wumpus_qtd:int=1, poco_qtd:int=3, gold_qtd:int=1):
        self.__mundo = [
            [Celula() for i in range(size) ] for i in range(size)
        ]
        self.__size = size
        
        for i in range(gold_qtd): self.__set_gold()
        for i in range(wumpus_qtd): self.__set_object('W', 'f')
        for i in range(poco_qtd): self.__set_object('P', 'b')
        
    def __str__(self):
        return self.get_world()
    
    def get_world(self) -> str:
        saida = ''

        for linha in self.__mundo:
            for valor in linha:
                saida += f' | {str(valor): ^3}'
            saida += ' |\n'

        return saida
    
    def get_percepcoes(self):
        saida = ''

        for linha in self.__mundo:
            for valor in linha:
                saida += f' | {valor.percepcao: ^3}'
            saida += ' |\n'

        return saida
    
    def __set_gold(self):
        pos_i, pos_j = 0, 0
        
        while True:
            pos_i = random.randint(0, self.__size - 1)
            pos_j = random.randint(0, self.__size - 1)

            if pos_i != 0 and pos_j != 0 :#and self.__mundo[pos_i][pos_j] == '':
                break
        
        self.__mundo[pos_i][pos_j].objeto = 'O'
        self.__mundo[pos_i][pos_j].percepcao += 'br'
        
    def __set_object(self, objeto:str, percepcao:str):
        pos_i, pos_j = 0, 0
        
        while True:
            pos_i = random.randint(0, self.__size - 1)
            pos_j = random.randint(0, self.__size - 1)

            if pos_i != 0 and pos_j != 0 and self.__mundo[pos_i][pos_j].objeto == '':
                break
        
        self.__mundo[pos_i][pos_j].objeto = objeto
        
        if pos_i + 1 < self.__size:
            self.__mundo[pos_i + 1][pos_j].percepcao += percepcao
        if pos_j + 1 < self.__size:
            self.__mundo[pos_i][pos_j + 1].percepcao += percepcao
        if pos_i - 1 >= 0:
            self.__mundo[pos_i - 1][pos_j].percepcao += percepcao
        if pos_j - 1 >= 0:
            self.__mundo[pos_i][pos_j - 1].percepcao += percepcao



    
    
if __name__ == '__main__':
    mapa = Ambiente()
    print(mapa)
    print()
    print(mapa.get_percepcoes())