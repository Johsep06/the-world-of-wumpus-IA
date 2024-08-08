from random import choice, randrange, shuffle

class Memory(object):
    def __init__(self, size: int) -> None:
        self.__size = size
        direcoes = {
            'N':'d',
            'S':'d',
            'L':'d',
            'O':'d',
            'C':'d',
            'V': 0
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
    
    def exibir(self) -> str:
        out = ''
        for line in self.__memory:
            out_aux = []
            for celula in line:
                if celula['C'] == 'd': out_aux.append(' ')
                elif celula['C'] == 'c': out_aux.append('-')
                else: out_aux.append(celula['C'])
            out += ' | '.join(out_aux) + '\n'
        return out

    def __bordas(self):
        for i in range(self.__size):
            self.__memory[0][i]['N'] = ' '
            self.__memory[i][0]['O'] = ' '
            self.__memory[self.__size - 1][i]['S'] = ' '
            self.__memory[i][self.__size - 1]['L'] = ' '

    
    def set_info(self, pos_i:int, pos_j:int, dado:str, in_center:bool=True):
        if in_center: self.__memory[pos_i][pos_j]['C'] = dado

        if self.__memory[pos_i][pos_j]['N'] != ' ':
            self.__memory[pos_i - 1][pos_j]['S'] = dado

        if self.__memory[pos_i][pos_j]['S'] != ' ':
            self.__memory[pos_i + 1][pos_j]['N'] = dado

        if self.__memory[pos_i][pos_j]['O'] != ' ':
            self.__memory[pos_i][pos_j - 1]['L'] = dado

        if self.__memory[pos_i][pos_j]['L'] != ' ':
            self.__memory[pos_i][pos_j + 1]['O'] = dado
    
    def del_info(self, pos_i:int, pos_j:int, dado:str):
        if dado in self.__memory[pos_i][pos_j]['C']:
            celula = self.__memory[pos_i][pos_j]

            aux = [s for s in celula['C']]
            aux.pop(celula['C'].index(dado))
            celula['C'] = ''.join(aux)

            self.__memory[pos_i][pos_j] = celula

        if dado in self.__memory[pos_i][pos_j]['N']:
            celula = self.__memory[pos_i - 1][pos_j]

            aux = [s for s in celula['S']]
            aux.pop(celula['S'].index(dado))
            celula['S'] = ''.join(aux)

            self.__memory[pos_i - 1][pos_j] = celula

        if dado in self.__memory[pos_i][pos_j]['S']:
            celula = self.__memory[pos_i + 1][pos_j]
            
            aux = [s for s in celula['N']]
            aux.pop(celula['N'].index(dado))
            celula['N'] = ''.join(aux)

            self.__memory[pos_i + 1][pos_j] = celula

        if dado in self.__memory[pos_i][pos_j]['O']:
            celula = self.__memory[pos_i][pos_j - 1]
            
            aux = [s for s in celula['L']]
            aux.pop(celula['L'].index(dado))
            celula['L'] = ''.join(aux)

            self.__memory[pos_i][pos_j - 1] = celula

        if dado in self.__memory[pos_i][pos_j]['L']:
            celula = self.__memory[pos_i][pos_j + 1]
            
            aux = [s for s in celula['O']]
            aux.pop(celula['O'].index(dado))
            celula['O'] = ''.join(aux)

            self.__memory[pos_i][pos_j + 1] = celula

    def set_anterior(self, pos_i:int, pos_j:int, dado:str, direcao:str):
        if direcao == 'N':
            self.__memory[pos_i - 1][pos_j]['S'] = dado
        
        elif direcao == 'S':
            self.__memory[pos_i + 1][pos_j]['N'] = dado

        elif direcao == 'L':
            self.__memory[pos_i][pos_j + 1]['O'] = dado

        elif direcao == 'O':
            self.__memory[pos_i][pos_j - 1]['L'] = dado

    def explorar(self, pos_i:int, pos_j:int, historico:str, flechas:int, w:str):
        celula = self.__memory[pos_i][pos_j]
        direcoes = ['S', 'L', 'N', 'O']
        moves = ''

        for i in direcoes:
            moves += celula[i]
        

        if moves.count('f') == 2: #? não lembro pq fiz esta linha:  and w == 'v'
            if 'f' in celula['N']:
                if 'f' in celula['L']:
                    self.set_info(pos_i - 1, pos_j + 1, 'W')
                else:
                    self.set_info(pos_i - 1, pos_j - 1, 'W')
            else:
                if 'f' in celula['L']:
                    self.set_info(pos_i + 1, pos_j + 1, 'W')
                else:
                    self.set_info(pos_i + 1, pos_j - 1, 'W')

        if moves.count('v') == 2:
            if 'v' in celula['N'] and 'v' in celula['S'] or 'v' in celula['L'] and 'v' in celula['O']:
                pass
            else:
                if 'v' in celula['N']:
                    if 'v' in celula['L']:
                        self.set_info(pos_i - 1, pos_j + 1, 'P')
                    else:
                        self.set_info(pos_i - 1, pos_j - 1, 'P')
                else:
                    if 'v' in celula['L']:
                        self.set_info(pos_i + 1, pos_j + 1, 'P')
                    else:
                        self.set_info(pos_i + 1, pos_j - 1, 'P')
                

        # if moves.count('v') >= 2 and 'vv' in moves:
        #     pos_v = moves.index('vv')

        #     if moves.count('v') == 3:
        #         self.set_info(pos_i, pos_j)


        # if 'W' in moves and flechas != 0:
        #     move = direcoes[moves.find('W')]

        #     if move == 'N':
        #         self.del_info(pos_i - 1, pos_j, 'W')

        #     elif move == 'S':
        #         self.del_info(pos_i + 1, pos_j, 'W')

        #     elif move == 'L':
        #         self.del_info(pos_i, pos_j + 1, 'W')

        #     elif move == 'O':
        #         self.del_info(pos_i, pos_j - 1, 'W')

        #     return move.lower()

        if 'c' in celula['C']:
            if 'd' in moves:
                for i in range(4):
                    if 'd' in celula[direcoes[i]]:
                        return direcoes[i]
                    
            elif 'S' in moves:
                aux_direcoes = 'NOSL'
                for i in range(4):
                    if 'S' in celula[aux_direcoes[i]]:
                        return aux_direcoes[i]
            
            elif 'c' in moves:
                for i in range(4):
                    if 'c' in celula[direcoes[i]]:
                        return direcoes[i]

            elif 'f' in moves or 'v' in moves:
                for i in range(4):
                    if 'f' in celula[direcoes[i]] or 'v' in celula[direcoes[i]]:
                        return direcoes[i]
            # else:
            #     result = -1
            #     for i in range(4):
            #         result += 1
            #         if moves[result] != ' ':
            #             break
            #     return direcoes[result]
            
        elif 'f' in celula['C']:
            if 'S' in moves and w == 'v':
                aux_direcoes = 'NOSL'
                for i in range(4):
                    if 'S' in celula[aux_direcoes[i]]:
                        return aux_direcoes[i]
                    
            elif 'c' in moves:
                for i in range(4):
                    if 'c' in celula[direcoes[i]]:
                        return direcoes[i]
                    
            elif 'd' in moves:
                for i in range(4):
                    if 'd' in celula[direcoes[i]]:
                        return direcoes[i]
            # else:
            #     result = -1
            #     for i in range(4):
            #         result += 1
            #         if moves[result] != ' ':
            #             break
            #     return direcoes[result]
            
        elif 'v' in celula['C']:
            if 'P' in moves:
                for i in range(4):
                    if not 'P' in celula[direcoes[i]]:
                        return direcoes[i]
                    
            elif 'c' in moves:
                for i in range(4):
                    if 'c' in celula[direcoes[i]]:
                        return direcoes[i]
                    
            elif 'S' in moves and w == 'v':
                aux_direcoes = 'NOSL'
                for i in range(4):
                    if 'S' in celula[aux_direcoes[i]]:
                        return aux_direcoes[i]
                    
            elif 'd' in moves:
                for i in range(4):
                    if 'd' in celula[direcoes[i]]:
                        return direcoes[i]
            # else:
            #     result = -1
            #     for i in range(4):
            #         result += 1
            #         if moves[result] != ' ':
            #             break
            #     return direcoes[result]

            # else:



            # if 'd' in moves:
            #     d = -1
            #     while True:
            #         d = randrange(0 ,4)
            #         if moves[d] == 'd' or moves[d] == 'c': break
                
            #     return direcoes[d]
            # elif 'c' in moves:
            #     d = -1
            #     while True:
            #         d = randrange(0 ,4)
            #         if moves[d] == 'd' or moves[d] == 'c': break
                
            #     return direcoes[d]
            # elif 'f' in moves:
            #     return direcoes[moves.find('f')]
            # elif 'S' in moves:
            #     return direcoes[moves.find('S')]
            # else:
            #     move = ''
            #     while True:
            #         move = choice(direcoes)
            #         if celula[move] != ' ': break
            #     return move


            
    def sair(self, pos_i:int, pos_j:int,flechas:int):
        celula = self.__memory[pos_i][pos_j]
        direcoes = 'NOSL'
        moves = ''

        for i in direcoes:
            moves += celula[i]

        if 'W' in moves and flechas != 0:
            return direcoes[moves.find('W')].lower()
        
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
                move = ''
                while True:
                    move = choice(direcoes)
                    if celula[move] != ' ': break
                return move
        