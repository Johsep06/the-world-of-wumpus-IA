from src.agente import Agente
from src.ambiente import Ambiente
from random import choice

class AgenteReativo2(Agente):
    __voltar = False
    def __init__(self, board: Ambiente) -> None:
        super().__init__(board)

        size = len(board)

        cel = {'N':'d', 'S':'d', 'L':'d', 'O':'d', 'C':'d'}
        self.__memoria = [[ cel.copy() for i in range(size) ] for i in range(size)]
        
        self.atualizar_memoria({'x':0, 'y':0}, 'S')
        
    def exibir_memoria(self):
        size = len(self.__memoria)

        for i in range(size):
            for j in range(size):
                print(i, j, self.__memoria[i][j], sep=' | ')
            print('\n')

    def atualizar_memoria(self, pos:dict[str,int], valor:str):
        posX = pos['x']
        posY = pos['y']
        size = len(self.__memoria)
        
        if self.__memoria[posY][posX]['C'] == 'd':
            self.__memoria[posY][posX]['C'] = valor
        else:
            self.__memoria[posY][posX]['C'] += valor

        if posY > 0:
            if self.__memoria[posY - 1][posX]['S'] == 'd':
                self.__memoria[posY - 1][posX]['S'] = valor
            else:
                self.__memoria[posY - 1][posX]['S'] += valor
        else:
            self.__memoria[posY][posX]['N'] = ''

        if posY < size:
            if self.__memoria[posY + 1][posX]['N'] == 'd':
                self.__memoria[posY + 1][posX]['N'] = valor
            else:
                self.__memoria[posY + 1][posX]['N'] += valor
        else:
            self.__memoria[posY][posX]['S'] = ''

        if posX > 0:
            if self.__memoria[posY][posX - 1]['L'] == 'd':
                self.__memoria[posY][posX - 1]['L'] = valor
            else:
                self.__memoria[posY][posX - 1]['L'] += valor
        else:
            self.__memoria[posY][posX]['O'] = ''

        if posX < size:
            if self.__memoria[posY][posX + 1]['O'] == 'd':
                self.__memoria[posY][posX + 1]['O'] = valor
            else:
                self.__memoria[posY][posX + 1]['O'] += valor
        else:
            self.__memoria[posY][posX]['L'] = ''

    def agir(self):
        pos_y, pos_x = self.get_pos()
        
        acoes = super().get_acoes()
        status = super().get_status()
        celula_atual = self.__memoria[pos_y][pos_x]

        if self.__voltar:
            pass

        if 'b' in status['percepção']:
            self.__voltar = True
            self.acao('x')

        # if 'f' in status['percepção'] or 'v' in status['percepção']:
        #     self.atualizar_memoria('status['percepção']')


