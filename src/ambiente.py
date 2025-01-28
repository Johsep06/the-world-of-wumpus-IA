import random

from celula import Celula

class Ambiente:
    def __init__(self, size:int=4, wumpus_qtd:int=1, poco_qtd:int=3, gold_qtd:int=1):
        '''
        Objeto Ambiente será responsável guardar e processar os dados do mundo de wumpus.
        - size:int = Tamanho do mundo, o mundo sempre será de tamanho quadrado.
        - wumpus_qtd:int é a quantidade de Wumpus no mundo.
        - poco_qtd:int = é a quantidade de Poços no mundo.
        - gold_qtd:int = é a quantidade de Ouro no mundo.
        '''
        self.__mundo = [
            [Celula() for i in range(size) ] for i in range(size)
        ] # Criação do mundo aplicado o objeto 'Celula' para cada posição.        

        self.__size = size # Salva o tamanho do mundo no objeto.
        
        for i in range(gold_qtd): 
            self.__set_gold() # Define a posição aleatória do objeto Ouro e sua percepção.
        for i in range(wumpus_qtd): 
            self.__set_object('W', 'f') # Define a posição aleatória do objeto Wumpus e suas percepções.
        for i in range(poco_qtd): 
            self.__set_object('P', 'b') # Define a posição aleatória do objeto Poço e suas percepções.
        
    def __str__(self): 
        '''
        Função que permite a converção do objeto em string.
        '''
        return self.get_world()
    
    def __len__(self): 
        '''
        Função que permite a a leitua do tamanho do mundo pela a função len.
        '''
        return self.__size
    
    def get_world(self) -> str:
        ''' 
        Função que exibe o estado do mundo pela prioridade da celula.
        '''
        saida = ''

        for linha in self.__mundo:
            for valor in linha:
                saida += f' | {str(valor): ^3}'
            saida += ' |\n'

        return saida
    
    def get_percepcoes(self): 
        '''
        Função que exibe apenas as percepções do mundo.
        '''
        saida = ''

        for linha in self.__mundo:
            for valor in linha:
                saida += f' | {valor.percepcao: ^3}'
            saida += ' |\n'

        return saida
    
    def __set_gold(self):
        '''
        Função que cálcula a posição aleatória do ouro e sua percepção.
        '''
        pos_i, pos_j = 0, 0 # inicia as variáveis da posição
        
        while True:
            pos_i = random.randint(0, self.__size - 1) # cálcula a posição i
            pos_j = random.randint(0, self.__size - 1)# cálcula a posição j

            e_posicao_inicial = pos_i == 0 and pos_j == 0 # verifica se as posição cálculada é a inicial
            posicao_esta_vazia = self.__mundo[pos_i][pos_j].objeto == ''# verifica se as posição cálculada está sem objetos

            if not e_posicao_inicial and posicao_esta_vazia:
                break
        
        self.__mundo[pos_i][pos_j].objeto = 'O' # seta objeto 'O' para representar o ouro.
        self.__mundo[pos_i][pos_j].percepcao += 'br' # senta a percepção br para representar o brilho
        
    def __set_object(self, objeto:str, percepcao:str):
        '''
        Função que cálcula a posição aleatória do ouro e sua percepção.
        '''
        pos_i, pos_j = 0, 0
        
        while True:
            pos_i = random.randint(0, self.__size - 1)
            pos_j = random.randint(0, self.__size - 1)

            if pos_i != 0 and pos_j != 0 and self.__mundo[pos_i][pos_j].objeto == '':
                break
        
        self.__mundo[pos_i][pos_j].objeto = objeto
        
        if pos_i + 1 < self.__size: # cálcula se existe a posição abaixo da cálculada
            self.__mundo[pos_i + 1][pos_j].percepcao += percepcao
            
        if pos_j + 1 < self.__size: # cálcula se existe a posição a direita da cálculada
            self.__mundo[pos_i][pos_j + 1].percepcao += percepcao
            
        if pos_i - 1 >= 0: # cálcula se existe a posição abaixo da cálculada
            self.__mundo[pos_i - 1][pos_j].percepcao += percepcao
            
        if pos_j - 1 >= 0:# cálcula se existe a posição a esquerda da cálculada
            self.__mundo[pos_i][pos_j - 1].percepcao += percepcao



    
    
if __name__ == '__main__': # funçao de testes do objeto
    mapa = Ambiente()
    print(mapa)
    print()
    print(mapa.get_percepcoes())