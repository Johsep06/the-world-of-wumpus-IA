from ambiente import Ambiente

board = Ambiente(4, 3)

board.set_out(True)
for b in board.get_board(): print(b)