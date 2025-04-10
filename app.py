from database import database
from src.ambiente import Ambiente
from src.sala import Sala
from src.agente_1 import Agente1
from src.agente_2 import Agente2
from src.memory import Memoria
from src.mundos_padroes import *

import random
from time import sleep

def gerar_e_salvar_mundo(size:int):
    while True:
        mundo.new(size)
        print(mundo)
        
        x = input('salvar mundo? ')
        
        if x == '0':
            database.save_mundo(mundo.to_dict())
            database.save_salas(mundo.salas_dict())
            break


# database.init_db()

if __name__ == '__main__':
    # database.init_db()
    mundo = Ambiente()
    mundo.load(**MUNDO_4_4)

    agente = Agente2(mundo)
    agente.new_memoria()

    # agente = AgenteAleatorio(mundo)
    
    print(mundo)
    while True:
        sleep(1)
        agente.agir()
        print(mundo)
        if agente.status() != '-':
            break
    
    # gerar_e_salvar_mundo(4)
    # mundo.load(**database.get_mundo(7))
    # agente = AgenteReativo(mundo)
    # agente.new_memoria()
    # print(mundo)
   
    # for _ in range(25):
    #     agente.decidir()
    #     print(mundo)
    #     sleep(1)
    # # gerar_e_salvar_mundo(4)