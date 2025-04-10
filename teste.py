# from queue import PriorityQueue
import random
from src.ambiente import Ambiente
from src.agente_3 import Agente3

# def exibir(values: dict[tuple, str]):
#     chaves = sorted(values, key= lambda x: (x[2], x[0], x[1]))
    
#     posicao_anterior = None
#     for posicao_atual in chaves:
#         if posicao_anterior is None:
#             posicao_anterior = posicao_atual
        
#         if posicao_atual[0] != posicao_anterior[0]:
#             print()
#         if posicao_atual[2] != posicao_anterior[2]:
#             print()
#         print(values[posicao_atual], end=' ')
#         posicao_anterior = posicao_atual
#     print()
    
# def show(lista):
#     linha = (min(lista, key=lambda x: x[0])[0], max(lista, key=lambda x: x[0])[0])
#     coluna = (min(lista, key=lambda x: x[1])[1], max(lista, key=lambda x: x[1])[1])
#     profundidade = (min(lista, key=lambda x: x[2])[2], max(lista, key=lambda x: x[2])[2])
    
#     for p in range(profundidade[0], profundidade[1] + 1):
#         print()
#         for l in range(linha[0], linha[1] + 1):
#             print()
#             for c in range(coluna[0], coluna[1] + 1):
#                 if (l, c, p) in lista:
#                     print(lista[(l, c, p)], end=' ')
#                 else:
#                     print(' ', end=' ')

ttt = {
    (0, 0, 0):'000', (0, 1, 0):'010', (0, 2, 0):'020', (0, 3, 0):'030',
    (1, 0, 0):'100', (1, 1, 0):'110', (1, 2, 0):'120', (1, 3, 0):'130',
    (2, 0, 0):'200', (2, 1, 0):'210', (2, 2, 0):'220', (2, 3, 0):'230',
    (3, 0, 0):'300', (3, 1, 0):'310', (3, 2, 0):'320', (3, 3, 0):'330',
    
    (0, 0, 1):'001', (0, 1, 1):'011', (0, 2, 1):'021', (0, 3, 1):'031', 
    (1, 0, 1):'101', (1, 1, 1):'111', (1, 2, 1):'121', (1, 3, 1):'131',
    (2, 0, 1):'201', (2, 1, 1):'211', (2, 2, 1):'221', (2, 3, 1):'231',
    (3, 0, 1):'301', (3, 1, 1):'311', (3, 2, 1):'321', (3, 3, 1):'331',
    
    (0, 0, 2):'002', (0, 1, 2):'012', (0, 2, 2):'022', (0, 3, 2):'032', 
    (1, 0, 2):'102', (1, 1, 2):'112', (1, 2, 2):'122', (1, 3, 2):'132',
    (2, 0, 2):'202', (2, 1, 2):'212', (2, 2, 2):'222', (2, 3, 2):'232',
    (3, 0, 2):'302', (3, 1, 2):'312', (3, 2, 2):'322', (3, 3, 2):'332',
    
    (0, 0, 3):'003', (0, 1, 3):'013', (0, 2, 3):'023', (0, 3, 3):'033', 
    (1, 0, 3):'103', (1, 1, 3):'113', (1, 2, 3):'123', (1, 3, 3):'133',
    (2, 0, 3):'203', (2, 1, 3):'213', (2, 2, 3):'223', (2, 3, 3):'233',
    (3, 0, 3):'303', (3, 1, 3):'313', (3, 2, 3):'323', (3, 3, 3):'333',
}

mundo = Ambiente()
mundo.new(10)

agente = Agente3(mundo)

gene = agente.evolucao(50, 1000)
print()
print((gene['resultado']))
print(*set(gene['resultado']), end=', ')
print(gene['pts'])
print(len(gene['cromossomo']))
# print(num_de_cruzamentos)
# print(agente.agir(50, 1000))