from ambiente import Ambiente
from agente import Agente

board = Ambiente(4, 3)
player = Agente(board)

print(board)
print(player.get_acoes())