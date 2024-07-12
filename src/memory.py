class Memory(object):
    def __init__(self, size: int) -> None:
        self.__size = size
        direcoes = {
            'N':'d',
            'S':'d',
            'L':'d',
            'O':'d',
            'C':'d'
        }

        self.__memory = [
          [
           direcoes.copy() for j in range(size)
          ]  for i in range(size)
        ]
        self.__bordas()

    def __str__(self) -> str:
        out = ''
        for i, line in enumerate(self.__memory):
            for j,cel in enumerate(line):
                out += f'{i, j} | {cel}.\n' #str(cel) + '\n'
            out += '\n'
        
        return out
    
    def __bordas(self):
        for i in range(self.__size):
            self.__memory[0][i]['N'] = ' '
            self.__memory[i][0]['O'] = ' '
            self.__memory[self.__size - 1][i]['S'] = ' '
            self.__memory[i][self.__size - 1]['L'] = ' '

    
    def set_info(self, pos_i:int, pos_j:int, dado:str):
        self.__memory[pos_i][pos_j]['C'] = dado

        if pos_i > 0:
            self.__memory[pos_i - 1][pos_j]['S'] = dado

        if pos_i < self.__size - 1:
            self.__memory[pos_i + 1][pos_j]['N'] = dado

        if pos_j > 0:
            self.__memory[pos_i][pos_j - 1]['L'] = dado

        if pos_j < self.__size - 1:
            self.__memory[pos_i][pos_j + 1]['O'] = dado

    def set_anterior(self, pos_i:int, pos_j:int, dado:str, direcao:str):
        if direcao == 'N':
            self.__memory[pos_i - 1][pos_j]['S'] = dado
        
        elif direcao == 'S':
            self.__memory[pos_i + 1][pos_j]['N'] = dado

        elif direcao == 'L':
            self.__memory[pos_i][pos_j + 1]['O'] = dado

        elif direcao == 'O':
            self.__memory[pos_i][pos_j - 1]['L'] = dado

    def explorar(self, pos_i:int, pos_j:int, historico:str):
        celula = self.__memory[pos_i][pos_j]
        direcoes = 'NSLO'
        moves = ''

        for i in direcoes:
            moves += celula[i]
        
        if len(historico) > 10:
            if 'NS'*5 == historico[-10:] or 'LO'*5 == historico[-10:]:
                result = -1
                for i in range(4):
                    result += 1
                    if moves[result] != ' ' and moves[result] != 'S':
                        break
                return direcoes[result]

        if 'c' in celula['C']:
            if 'd' in moves:
                return direcoes[moves.find('d')]
            elif 'c' in moves:
                return direcoes[moves.find('c')]
            elif 'S' in moves:
                return direcoes[moves.find('S')]
            else:
                result = -1
                for i in range(4):
                    result += 1
                    if moves[result] != ' ':
                        break
                return direcoes[result]
            
        elif 'f' in celula['C']:
            if 'S' in moves:
                return direcoes[moves.find('S')]
            elif 'c' in moves:
                return direcoes[moves.find('c')]
            elif 'd' in moves:
                return direcoes[moves.find('d')]
            else:
                result = -1
                for i in range(4):
                    result += 1
                    if moves[result] != ' ':
                        break
                return direcoes[result]
            
        elif 'v' in celula['C']:
            if 'S' in moves:
                return direcoes[moves.find('S')]
            elif 'c' in moves:
                return direcoes[moves.find('c')]
            elif 'd' in moves:
                return direcoes[moves.find('d')]
            else:
                result = -1
                for i in range(4):
                    result += 1
                    if moves[result] != ' ':
                        break
                return direcoes[result]


            
    def sair(self, pos_i:int, pos_j:int):
        celula = self.__memory[pos_i][pos_j]
        direcoes = 'NLSO'
        moves = ''

        for i in direcoes:
            moves += celula[i]
        
        if 'S' in moves:
            return direcoes[moves.find('S')]
        
        elif 'c' in moves:
            return direcoes[moves.find('c')]
        
        elif 'd' in moves:
            return direcoes[moves.find('d')]

        elif 'v' in moves:
            return direcoes[moves.find('v')]

        elif 'f' in moves:
            return direcoes[moves.find('f')]
        else:
                result = -1
                for i in range(4):
                    result += 1
                    if moves[result] != ' ':
                        break
                return direcoes[result]
        