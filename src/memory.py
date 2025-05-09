# from src.a_estrela import a_estrela

from queue import PriorityQueue
from random import choice

class Memoria:
    def __init__(self):
        self.__memoria:dict[tuple[int, int, int], str] = {}

    def to_dict(self):
        dados = []
        for posicao in self.__memoria:
            dados.append({
                'pos_i':posicao[0], 
                'pos_j':posicao[1], 
                'simbolo':self.__memoria[posicao]
            })
            
        return dados

    def new(self,):
        self.__memoria = {(0, 0, 0):'S'}
    
    def expendir_salas(self, posicao:tuple[int, int, int], direcoes:str):
        sentidos = {
            'N':(-1, 0, 0),
            'S':(+1, 0, 0),
            'L':(0, +1, 0),
            'O':(0, -1, 0),
            'C':(0, 0, -1),
            'B':(0, 0, 1),
        }
        
        for direcao in direcoes:
            sentido = sentidos[direcao]
            nova_posicao = (
                posicao[0] + sentido[0],
                posicao[1] + sentido[1],
                posicao[2] + sentido[2]
            )
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
        saida += self.__memoria[posicao]
        
        while not fila.empty():
            posicao = fila.get()
            if linha == posicao[0]:
                saida += ' ' + self.__memoria[posicao]
            else: 
                linha = posicao[0]
                saida += '\n' + self.__memoria[posicao]

        return saida

    def get_memoria(self):
        return self.__memoria

    def marcar_mapa(self, posicao:tuple[int, int, int], simbolo:str):
        if self.__memoria[posicao].lower() == 'd':
            self.__memoria[posicao] = simbolo
        elif '!' in self.__memoria[posicao] or '?' in self.__memoria[posicao]:
            self.__memoria[posicao] = simbolo
        elif simbolo == '-':
            if self.__memoria[posicao].lower() != 'd':
                return
            self.__memoria[posicao] = simbolo
        else:
            self.__memoria[posicao] += simbolo
            
    def suspeitar_salas(self, posicao:tuple[int, int, int], simbolo:str):
        salas_suspeitas = []
        for i,j,k in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)]:
            posicao_suspeita = (posicao[0] + i, posicao[1] + j, posicao[2] + k)

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
        for i,j,k in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)]:
            posicao_segura = (posicao[0] + i, posicao[1] + j, posicao[2] + k)
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
    
    def buscar(self, valor):
        localizacao = None
        for posicao in self.__memoria:
            if valor in self.__memoria[posicao]:
                localizacao = posicao
                break

        return localizacao
    
    def buscar_maior_peso(self, valor):
        posicoes_com_pesos = {}
        
        for posicao in self.__memoria:
            if valor in self.__memoria[posicao]:
                peso = self.__memoria[posicao].count(valor)
                posicoes_com_pesos[posicao] = peso
        
        maior_peso = 0
        localizacao = None
        
        for posicao in posicoes_com_pesos:
            if posicoes_com_pesos[posicao] > maior_peso:
                maior_peso = posicoes_com_pesos[posicao]
                localizacao = posicao
        return localizacao
    
    def sala_aleatoria(self, posicao_atual):
        localizacao = None
        posicoes = list(self.__memoria.keys())

        while True:
            localizacao = choice(posicoes)
            
            ha_poco_na_sala = self.__memoria[localizacao] == 'P'
            e_sala_atual = localizacao == posicao_atual

            if ha_poco_na_sala or e_sala_atual:
                continue
            break
        
        return localizacao
            
    def checar_sala(self, posicao:tuple[int, int]):
        return self.__memoria[posicao]         
    
if __name__ == '__main__':
    memoria = Memoria()
    memoria.new()
    print(memoria.to_dict())