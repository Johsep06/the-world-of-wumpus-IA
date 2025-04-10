from src.agente import Agente
import random

class Agente3(Agente):
    def __init__(self, mundo):
        super().__init__(mundo)
        self.set_tipo()
        self.gene = ''
    
    def set_tipo(self):
        self._tipo = 3
        
    def criar_genes(self, qtd:int):
        genes = []
        
        tamanho_maximo = 20
        
        for i in range(qtd):
            gene = {
                'cromossomo':'',
                'resultado':[],
                'pts':0,
            }
            tamanho_do_gene = random.randint(4, tamanho_maximo)
            
            for _ in range(tamanho_do_gene):
                acao = random.choice('NSLOCB')
                sorteio = random.randint(1, 50)
                if sorteio > 45:
                    acao = acao.lower()
                gene['cromossomo'] += acao
            genes.append(gene)
            
        return genes
    
    def avaliacao(self, gene:dict):
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

        for g in gene['cromossomo']:
            direcao = direcoes[g.upper()]  # Obtém a direção correspondente ao gene

            if g.islower():  # Se o gene for minúsculo, o agente atira
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

                if objeto in ['P', '-', 'S', 'F']:  # Verifica outros objetos (poço, espaço vazio, saída)
                    valor = objeto

                resultado.append(valor)  # Adiciona o valor ao resultado

        gene['resultado'] = resultado  # Retorna o resultado da avaliação

    def fitness(self, gene: dict):
        # Inicializa a pontuação
        tem_ouro = False
        pontuacoes = {
            # Pegou ouro
            'O':+15000,
            # Matou o Wumpus
            'X':+200,
            # Nada aconteceu
            '-':-0.01,
            # Morreu por Wumpus
            'W':-800,
            # Morreu por poço
            'P':-800,
            # Saiu do mapa
            'F':-1000,
            # Tiro errado
            'x':-10,
            # Vitória
            'V':10000
        }
        pts = 0
        # Percorre o resultado e calcula a pontuação
        for simbolo in gene['resultado']:
            pontuacoes['S'] = pontuacoes['V'] if tem_ouro else pontuacoes['-']
            if len(simbolo) == 1:
                pts += pontuacoes[simbolo]
            else:
                for s in simbolo:
                    pts += pontuacoes[s]
            
            if simbolo == 'O': tem_ouro = True

        gene['pts'] = pts

    def cruzamento(self, gene_A:dict, gene_B:dict):
        corte_A = int(len(gene_A) / 2) #random.randint(1, (len(gene_A['cromossomo']) - 1))
        corte_B = int(len(gene_B) / 2) #random.randint(1, (len(gene_B['cromossomo']) - 1))
        
        inicio_A = gene_A['cromossomo'][:corte_A]
        resto_B = gene_B['cromossomo'][corte_B:]

        novo_gene = {
            'cromossomo':inicio_A + resto_B,
            'resultado':[],
            'pts':0,
        }
        
        return novo_gene
    
    def mutacao(self, gene:dict):
        acoes = 'NSLOCB'
        acao_escolhida = random.choice(acoes)
        
        sorteio = random.randint(1, 50)
        if sorteio > 45:
            acao_escolhida = acao_escolhida.lower()
        
        posicao = random.randint(0, len(gene['cromossomo']) - 1)
        novo_cromossomo = gene['cromossomo'][:posicao] + acao_escolhida + gene['cromossomo'][posicao + 1:]
        
        gene['cromossomo'] = novo_cromossomo

        gene['resultado'] = []
        self.avaliacao(gene)

        gene['pts'] = 0
        self.fitness(gene)

    def evolucao(self, populacao: int, geracoes: int):
        genes = self.criar_genes(populacao)

        for g in genes:
            self.avaliacao(g)
            self.fitness(g)

        genes.sort(key=lambda x: x['pts'], reverse=True)

        for geracao in range(geracoes):
            num_de_cruzamentos = max(1, int(populacao*0.85))
            num_de_cruzamentos = num_de_cruzamentos if num_de_cruzamentos % 2 == 0 else num_de_cruzamentos - 1

            # if geracao % 100 == 0:
            #     novos_genes = self.criar_genes(int(populacao/5))
            #     for ng in novos_genes:
            #         self.avaliacao(ng)
            #         self.fitness(ng)
            #     genes.extend(novos_genes)
            
            for i in range(0, num_de_cruzamentos, 2):
                filho:dict = None
                try:
                    filho = self.cruzamento(genes[i], genes[i + 1])
                except IndexError:
                    continue
                self.avaliacao(filho)
                self.fitness(filho)
                genes.append(filho)

            num_de_mutacoes = max(1, int(len(genes)*0.05))
            inices_mutados = set()
            
            for i in range(num_de_mutacoes):
                while True:
                    indice = random.choice(range(0, len(genes)))
                    if indice not in inices_mutados:
                        inices_mutados.add(indice)
                        break

            for i in inices_mutados:
                self.mutacao(genes[i])
            
            genes.sort(key=lambda x: x['pts'], reverse=True)

            genes = genes[:populacao]
            print(f'Geração: {geracao} de {geracoes}.', end='\r')
        
        self.gene = genes[0]['cromossomo']
        return genes[0]
    
    def agir(self):
        ...