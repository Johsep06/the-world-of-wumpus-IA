from src.agente import Agente
from src.ambiente import Ambiente
from src.memory import Memoria
from src.a_estrela import a_estrela

class Agente2(Agente):
    def __init__(self, mundo:Ambiente):
        super().__init__(mundo)
        self.set_tipo()
        self._memoria = None

    def set_tipo(self):
        self._tipo = 2
        
    def new_memoria(self):
        self._memoria = Memoria()
        self._memoria.new()
    
    def __decidir(self):
        direcoes = self._mundo.direcoes_possiveis(self.id)
        status_atual = self._mundo.check_status(self.id, self.inventario)
        sala_atual = self._mundo.get_coordenada(self.id)

        self._memoria.expendir_salas(sala_atual, direcoes)
        
        percepcao = status_atual['percepcao']
        if percepcao == '-':
            self._memoria.assegurar_salas(sala_atual)
            
        if 'f' in percepcao and self._memoria.checar_sala(sala_atual) == 'D':
            self._memoria.suspeitar_salas(sala_atual, 'W')

        if 'br' in percepcao and self._memoria.checar_sala(sala_atual).upper() != 'O':
            self._memoria.marcar_mapa(sala_atual, 'O')
            if 'br' == percepcao:
                self._memoria.assegurar_salas(sala_atual)
            
            if self._mundo.pegar(self.id) == 'O':
                self.inventario['ouro'] += 1 
        if 'b' in percepcao and self._memoria.checar_sala(sala_atual) == 'D':
            qtd_de_brisa = percepcao.count('b')
            qtd_de_brilho = percepcao.count('br')
            print(percepcao)
            
            if qtd_de_brisa - qtd_de_brilho >= 0:
                self._memoria.suspeitar_salas(sala_atual, 'P')
                
        if status_atual['status'] == 'P':
            self._memoria.marcar_mapa(sala_atual, 'P')
        elif 'W' in status_atual['status']:
            self._memoria.marcar_mapa(sala_atual, 'W')
        else: 
            self._memoria.marcar_mapa(sala_atual, '-')
        
        atirar = False
            
        proxima_posicao = self._memoria.buscar('W')	
        if proxima_posicao is not None:
            atirar = True
            if proxima_posicao == sala_atual:
                atirar = False
                proxima_posicao = None
        if proxima_posicao is None:
            proxima_posicao = self._memoria.buscar('D')
        if proxima_posicao is None:
            proxima_posicao = self._memoria.buscar_maior_peso('?')
        if proxima_posicao is None:
            proxima_posicao = self._memoria.sala_aleatoria(sala_atual)
         
        

        caminho = a_estrela(sala_atual, proxima_posicao, self._memoria.get_memoria(), ['W', 'P'])

        if atirar and len(caminho) == 1:
            print(f'tiro para o {caminho.lower()}')
            self._mundo.atirar(self.id, caminho.lower())
        else:
            self._mundo.mover(self.id, caminho[0])
        print(self._memoria)
        
    def agir(self):
        self.__decidir()