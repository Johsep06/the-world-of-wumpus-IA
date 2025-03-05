from queue import PriorityQueue

def __h_score(pos_inicial:tuple[int, int, int], pos_final:tuple[int, int, int]) -> int:
    distacia_i = abs(pos_inicial[0] - pos_final[0])
    distacia_j = abs(pos_inicial[1] - pos_final[1])
    distacia_k = abs(pos_inicial[2] - pos_final[2])

    return distacia_i + distacia_j + distacia_k

def __expandir_posicao(posicao:tuple[int, int, int], mapa) -> list[tuple[int, int]]:
    vizinhos = []
    
    for i,j,k in [(-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, 1), (0, 0, -1)]:
        vizinho = (posicao[0] + i, posicao[1] + j, posicao[2] + k)
        if not vizinho in mapa:
            continue
        
        vizinhos.append((posicao[0] + i, posicao[1] + j, posicao[2] + k))
    
    return vizinhos

def __converter_em_direcoes(inicio:tuple[int,int], caminho:dict[tuple, tuple]) -> str:
    direcao = ''
    direcoes = {
            (-1, 0, 0):'N',
            (1, 0, 0):'S',
            (0, 1, 0):'L',
            (0, -1, 0):'O',
            (0, 0, -1):'C',
            (0, 0, 1):'B',
        }
    
    posicao = inicio
    for _ in range(len(caminho)):
        i = caminho[posicao][0] - posicao[0]
        j = caminho[posicao][1] - posicao[1]
        k = caminho[posicao][2] - posicao[2]
        
        direcao += str(direcoes[(i,j,k)])
        posicao = caminho[posicao]

    return direcao

def a_estrela(inicio:tuple[int, int, int], destino:tuple[int, int, int], mapa:dict[tuple[int, int, int], str], obstaculos:list[str]) -> str:
    
    f_score = {celula:float('inf') for celula in list(mapa.keys())}
    g_score:dict[tuple, int] = {}
    
    g_score[inicio] = 0
    f_score[inicio] =  g_score[inicio] + __h_score(inicio, destino)
    
    fila = PriorityQueue()
    item = (f_score[inicio], __h_score(inicio, destino), inicio)
    fila.put(item)
    
    caminho = {}
    
    while not fila.empty():
        posicao = fila.get()[2]
        
        if posicao == destino:
            break
        
        for nova_posicao in __expandir_posicao(posicao, mapa):
            posicao_livre = True

            for obstaculo in obstaculos:
                if obstaculo in mapa[nova_posicao]:
                    posicao_livre = False
                    break
            if not posicao_livre:
                continue    
            # if 'P' in mapa[nova_posicao]:
            #     continue
            # if 'W' in mapa[nova_posicao]:
            #     continue
            
            novo_g_score = g_score[posicao] + 1
            novo_f_score = novo_g_score + __h_score(nova_posicao, destino)
            
            if novo_f_score < f_score[nova_posicao]:
                f_score[nova_posicao] = novo_f_score
                g_score[nova_posicao] = novo_g_score

                item = (novo_f_score, __h_score(nova_posicao, destino), nova_posicao)
                fila.put(item)
                caminho[nova_posicao] = posicao
                
    caminho_final = {}
    posicao_analizada = destino

    while posicao_analizada != inicio:
        caminho_final[caminho[posicao_analizada]] = posicao_analizada
        posicao_analizada = caminho[posicao_analizada]
    
    rota = __converter_em_direcoes(inicio, caminho_final)
    return rota


if __name__ == '__main__':
    rota = {(0,0):(0,1), (1,0):(0,0)}
    s = __converter_em_direcoes((1,0), rota)
    print(s)