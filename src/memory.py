# from src.a_estrela import a_estrela

from queue import PriorityQueue

class Memoria:
    def __init__(self):
        self.__memoria:dict[tuple[int, int], str] = {}

    def new(self,):
        self.__memoria = {(0, 0):'-'}
    
    def expendir_salas(self, posicao:tuple[int, int], direcoes:str):
        sentidos = {
            'N':(-1, 0),
            'S':(+1, 0),
            'L':(0, +1),
            'O':(0, -1)
        }
        
        for direcao in direcoes:
            sentido = sentidos[direcao]
            nova_posicao = (posicao[0] + sentido[0], posicao[1] + sentido[1])
            if nova_posicao in self.__memoria:
                continue
            self.__memoria[nova_posicao] = 'd'
    
    def __str__(self):
        saida = ''
        fila = PriorityQueue()
        
        for posicao in self.__memoria:
            fila.put(posicao)

        posicao = fila.get()
        linha = posicao[0]
        print(posicao, type(posicao))
        saida += self.__memoria[posicao]
        
        while not fila.empty():
            posicao = fila.get()
            if linha == posicao[0]:
                saida += ' ' + self.__memoria[posicao]
            else: 
                linha = posicao[0]
                saida += '\n' + self.__memoria[posicao]

        return saida

    def marcar_mapa(self, posicao:tuple[int, int], simbolo:str):
        if self.__memoria[posicao] == 'd':
            self.__memoria[posicao] = simbolo
        elif '!' in self.__memoria[posicao] or '?' in self.__memoria[posicao]:
            self.__memoria[posicao] = simbolo
        else:
            self.__memoria[posicao] += simbolo
            
    def suspeitar_salas(self, posicao:tuple[int, int], simbolo:str):
        salas_suspeitas = []
        for i,j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            posicao_suspeita = (posicao[0] + i, posicao[1] + j)

            if posicao_suspeita not in self.__memoria:
                continue
            
            posicao_desconhecida = self.__memoria[posicao_suspeita] == 'd'
            posicao_ja_suspeita_w = '?' in self.__memoria[posicao_suspeita]
            posicao_ja_suspeita_p = '!' in self.__memoria[posicao_suspeita]
            
            if posicao_desconhecida or posicao_ja_suspeita_p or posicao_ja_suspeita_w:
                salas_suspeitas.append(posicao_suspeita)
            
        if len(salas_suspeitas) == 0:
            return
        elif len(salas_suspeitas) == 1:
            self.__memoria[salas_suspeitas[0]] = simbolo
        else:
            marcacao = {'W':'?', 'P':'!'}
            for sala in salas_suspeitas:
                if self.__memoria[sala] == 'd':
                    self.__memoria[sala] = marcacao[simbolo]
                else: 
                    self.__memoria[sala] += marcacao[simbolo]

    def assegurar_salas(self, posicao:tuple[int, int]):
        salas_seguras = []
        for i,j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            posicao_segura = (posicao[0] + i, posicao[1] + j)
            if posicao_segura not in self.__memoria:
                continue

            posicao_desconhecida = self.__memoria[posicao_segura] == 'd'
            posicao_ja_suspeita_w = '?' in self.__memoria[posicao_segura]
            posicao_ja_suspeita_p = '!' in self.__memoria[posicao_segura]
            
            if posicao_desconhecida or posicao_ja_suspeita_p or posicao_ja_suspeita_w:
                salas_seguras.append(posicao_segura)
            
        if len(salas_seguras) == 0:
            return
        else:
            for sala in salas_seguras:
                self.__memoria[sala] = 'D'
                
if __name__ == '__main__':
    memoria = Memoria()
    memoria.new(4)
    memoria.marcar_mapa((2,1), '-')
    memoria.assegurar_salas((1,3))
    memoria.suspeitar_salas((2,2), 'W')
    print(memoria)