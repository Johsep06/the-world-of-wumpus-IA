class Celula(object):
    def __init__(self, value: str) -> None:
        self.__value = value
        self.__objeto = ''
        self.__percepcao = ['']
        self.__out = value
    
    
    def setValue(self, value: str):self.__value = value
    def setObjeto(self, objeto:str):self.__objeto = objeto
    def setPercepcao(self, percepcao: str):
        try:
            self.__percepcao.remove(' ')
        except:
            pass

        if percepcao in self.__percepcao: return

        self.__percepcao += percepcao

    def setOut(self, id: int):
        '''
        0 - para exibir o valor padrão da célula\n
        1 - para exibir o objeto da célula\n
        2 - pra exibir a percepção da célula
        '''
        if id == 0:
            self.__out = self.__value
        elif id == 1:
            self.__out = self.__objeto
        elif id == 2:
            self.__out = ''.join(self.__percepcao)

    def getOut(self) -> str: return self.__out
    def getValue(self) -> str: return self.__value
    def getObjeto(self) -> str: return self.__objeto
    def getPercepcao(self) -> str: return ''.join(self.__percepcao)