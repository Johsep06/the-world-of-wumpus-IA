from src.agente import Agente
from src.ambiente import Ambiente
from src.memory import Memory

class AgenteReativo2(Agente):
    def __init__(self, board: Ambiente) -> None:
        super().__init__(board, tipo_agente=2)

        size = len(board)
        self.__memory = Memory(size)
        self.__voltar = False
        

    def agir(self):
        pos_i, pos_j = self.get_pos()
        status = super().get_status()

        if status['percepcao'] == '':
            self.__memory.set_info(pos_i, pos_j, 'c')
        else:
            self.__memory.set_info(pos_i, pos_j, status['percepcao'])

        if self.__voltar:
            move = self.__memory.sair(pos_i, pos_j)
            self.acao(move)

        else:
            if 'b' in status['percepcao']:
                self.__voltar = True
                self.acao('x')
            else:
                historico = self.get_status()['historico']
                w = self.get_status()['wumpus']
                move = self.__memory.explorar(pos_i, pos_j, historico, self.get_flechas(), w)

                if not('v' in  status['percepcao'] or 'f' in  status['percepcao']):
                    self.__memory.set_anterior(pos_i, pos_j, 'S', move)
                self.acao(move)
                

        

        # if 'f' in status['percepção'] or 'v' in status['percepção']:
        #     self.atualizar_memoria('status['percepção']')


