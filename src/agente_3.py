from src.agente import Agente
import random

class Agente3(Agente):
    def __init__(self, mundo):
        super().__init__(mundo)
        self.set_tipo()
    
    def set_tipo(self):
        self._tipo = 3
        
    def criar_genes(self, qtd:int):
        genes = []
        
        tamanho_maximo = int(len(self._mundo) * 1.5)
        
        for i in range(qtd):
            gene = {
                'cromossomo':'',
                'pts':0,
            }
            tamanho_do_gene = random.randint(2, tamanho_maximo)
            
            for _ in range(tamanho_do_gene):
                gene['cromossomo'] += random.choice('NSLOCBnslocb')
            genes.append(gene)
            
        return genes
    
    def avaliacao(self, cromossomo: str):
        direcoes = {
            'N': (-1, 0, 0),
            'S': (1, 0, 0),
            'O': (0, -1, 0),
            'L': (0, 1, 0),
            'C': (0, 0, -1),
            'B': (0, 0, 1)
        }

        posicao = (0, 0, 0)  # Posição inicial do agente
        posicoes_livre_de_wumpus = set()  # Posições onde o Wumpus foi eliminado
        posicoes_sem_ouro = set()  # Posições onde o ouro foi coletado
        resultado = []  # Resultado da avaliação

        for gene in cromossomo:
            direcao = direcoes[gene.upper()]  # Obtém a direção correspondente ao gene

            if gene.islower():  # Se o gene for minúsculo, o agente atira
                posicao_avaliada = (
                    posicao[0] + direcao[0],
                    posicao[1] + direcao[1],
                    posicao[2] + direcao[2],
                )
                objeto = self._mundo.checar_posicao(posicao_avaliada)  # Verifica o objeto na posição
                if 'W' in objeto and posicao_avaliada not in posicoes_livre_de_wumpus:
                    resultado.append('X')  # Wumpus foi morto
                    posicoes_livre_de_wumpus.add(posicao_avaliada)  # Marca a posição como livre de Wumpus
                else:
                    resultado.append('x')  # Wumpus não foi morto
            else:  # Se o gene for maiúsculo, o agente se move
                posicao = (
                    posicao[0] + direcao[0],
                    posicao[1] + direcao[1],
                    posicao[2] + direcao[2],
                )

                objeto = self._mundo.checar_posicao(posicao)  # Verifica o objeto na nova posição
                valor = ''

                if 'W' in objeto:
                    if posicao not in posicoes_livre_de_wumpus:
                        valor += 'W'  # Wumpus está na posição
                    else:
                        valor += '-'

                if 'O' in objeto:
                    if posicao not in posicoes_sem_ouro:
                        valor += 'O'  # Ouro está na posição
                        posicoes_sem_ouro.add(posicao)  # Marca a posição como sem ouro
                    else:
                        valor += '-'  # Ouro já foi coletado

                if objeto in ['P', '-', 'S']:  # Verifica outros objetos (poço, espaço vazio, saída)
                    valor = objeto

                resultado.append(valor)  # Adiciona o valor ao resultado

        return resultado  # Retorna o resultado da avaliação