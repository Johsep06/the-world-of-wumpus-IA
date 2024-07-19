import pickle

def serializar(objeto, caminhoArquivo: str):
    '''
    A função Serializar compacta objetos em arquivos binários.

    Obs: a extenção do arquivo precisa ser informana na string nome.
    '''
    with open(caminhoArquivo, 'wb') as arquivo:
        pickle.dump(objeto, arquivo)

def desserializar(caminhoArquivo: str):
    '''
    A função Desserializar descompacta arquivos binários em objetos.

    Obs: a extenção do arquivo precisa ser informana na string nome.
    '''
    with open(caminhoArquivo, 'rb') as arquivo:
        objeto = pickle.load(arquivo)
        return objeto