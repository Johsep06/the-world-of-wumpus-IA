from src.ambiente import Ambiente
from src.agente import Agente
from src.agente_aleatorio import AgenteAleatorio

class Game(object):
    def __init__(self) -> None:
       pass

    def __len__(self):
        return len(self.__board)
    
    def new_game(self, size: int, agente:int):
        '''
        agente = 1:Agente Aleatório; 2: Agente Reativo, 3:Agente de Aprendizagem
        '''
        try:
            del(self.__board)
            del(self.__ia)
        except AttributeError:
            pass

        # Calcula o número de "pocos" (obstáculos) no tabuleiro.
        pocos = int(size ** 2 * (3 / 16))

        # Cria um novo ambiente com o tamanho especificado e a quantidade de "pocos".
        self.__board = Ambiente(size, pocos)

        # Cria um novo agente com base no tipo especificado.
        if agente == 1:
            self.__ia = AgenteAleatorio(self.__board)
        # elif agente == 2:
        #     self.__ia = AgenteReativo(self.__board)
        # elif agente == 3:
        #     self.__ia = AgenteAprendizagem(self.__board)
        else:
            raise ValueError("Tipo de agente inválido. Use 1 (Aleatório), 2 (Reativo) ou 3 (Aprendizagem).")
        

    def tabuleiro(self) -> list[list[str]]:
        self.__board.set_out(True)
        return self.__board.getMap()
    
    def get_percepcoes(self) -> list[list[str]]:
        return self.__board.get_percepcoes()

    def jogada(self) -> None:
        self.__ia.agir()

    def get_relatorio(self) -> dict:
        relatorio = self.__ia.get_status()
        relatorio['bag'] = self.__ia.get_bag()
        relatorio['flecha'] = self.__ia.get_flechas()

        return relatorio

# def novo_jogo(size: int):
#     global board
#     pocos = int(size * size * (3/16))

#     board = None
#     board = Ambiente(size, pocos)