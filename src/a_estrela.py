from queue import PriorityQueue

def h_score(pos_inicial:tuple[int, int], pos_final:tuple[int, int]) -> int:
    distacia_i = abs(pos_inicial[0] - pos_final[0])
    distacia_j = abs(pos_inicial[1] - pos_final[1])

    return distacia_i + distacia_j

def expandir_posicao(posicao:tuple[int, int], tamanho:int) -> list[tuple[int, int]]:
    vizinhos = []
    
    for i,j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if not 0 <= posicao[0] + i < tamanho:
            continue
        if not 0 <= posicao[1] + j < tamanho:
            continue
        
        vizinhos.append((posicao[0] + i, posicao[1] + j))
    
    return vizinhos

def converter_em_direcoes(inicio:tuple[int,int], caminho:dict[tuple, tuple]) -> str:
    direcao = ''
    direcoes = {
            (-1, 0):'N',
            (1, 0):'S',
            (0, 1):'L',
            (0, -1):'O',
        }
    
    posicao = inicio
    for _ in range(len(caminho)):
        i = abs(posicao[0] - caminho[posicao][0])
        j = abs(posicao[1] - caminho[posicao][1])
        
        direcao += str(direcoes[(i,j)])
        posicao = caminho[posicao]

    return direcao

def a_estrela(inicio:tuple[int, int], destino:tuple[int, int], mapa:dict[tuple[int, int], str], tamanho:int) -> str:
    
    f_score = {celula:float('inf') for celula in list(mapa.keys())}
    g_score:dict[tuple, int] = {}
    
    g_score[inicio] = 0
    f_score[inicio] =  g_score[inicio] + h_score(inicio, destino)
    
    fila = PriorityQueue()
    item = (f_score[inicio], h_score(inicio, destino), inicio)
    fila.put(item)
    
    caminho = {}
    
    while not fila.empty():
        posicao = fila.get()[2]
        
        if posicao == destino:
            break
        
        for nova_posicao in expandir_posicao(posicao, tamanho):
            if 'P' in mapa[nova_posicao]:
                continue
            if 'W' in mapa[nova_posicao]:
                continue
            
            novo_g_score = g_score[posicao] + 1
            novo_f_score = novo_g_score + h_score(nova_posicao, destino)
            
            if novo_f_score < f_score[nova_posicao]:
                f_score[nova_posicao] = novo_f_score
                g_score[nova_posicao] = novo_g_score

                item = (novo_f_score, h_score(nova_posicao, destino), nova_posicao)
                fila.put(item)
                caminho[nova_posicao] = posicao
                
    caminho_final = {}
    posicao_analizada = destino

    while posicao_analizada != inicio:
        caminho_final[caminho[posicao_analizada]] = posicao_analizada
        posicao_analizada = caminho[posicao_analizada]
    
    rota = converter_em_direcoes(inicio, caminho_final)
    return rota


if __name__ == '__main__':
    mundo = {
        (0,0):'',
        (0,1):'',
        (0,2):'',
        (0,3):'',
        (1,0):'',
        (1,1):'',
        (1,2):'',
        (1,3):'W',
        (2,0):'P',
        (2,1):'',
        (2,2):'P',
        (2,3):'P',
        (3,0):'',
        (3,1):'',
        (3,2):'',
        (3,3):'0',
    }
    
    print(a_estrela((0,0), (3,3), mundo, 4))