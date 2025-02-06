# import mysql.connector
import pymysql
from pathlib import Path

from database.querys import init, insert, select
from database.config_db import DB_CONFIG # Dicionario com as Configuações do MySQL

def init_db():
    try:
        # Conecta ao banco de dados MySQL
        # connection = mysql.connector.connect(**DB_CONFIG)
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()
        
        # Cria as tabelas
        cursor.execute(init.DATABASE)
        connection.commit()
        cursor.execute(init.USE_DATABASE)
        connection.commit()
        cursor.execute(init.TABLE_MUNDO)
        connection.commit()
        cursor.execute(init.TABLE_SALA)
        connection.commit()
        cursor.execute(init.TABLE_AGENTE)
        connection.commit()
    except Exception as e:
        print('Erro ao criar o banco de dados:', str(e))
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com o MySQL encerrada.")

def get_mundo_qtd() -> int:
    mundo_qtd = None
    try:
        # Conecta ao banco de dados MySQL
        # connection = mysql.connector.connect(**DB_CONFIG)
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()
        
        cursor.execute(init.USE_DATABASE)
        connection.commit()
        
        # Executa a consulta para obter a quantidade de mundos
        cursor.execute(select.MUNDO_QTD)
        mundo_qtd = cursor.fetchone()
        
    except Exception as e:
        print('Erro ao acessar o banco de dados:', str(e))
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com o MySQL encerrada.")
    
    return mundo_qtd[0] if mundo_qtd else 0

def add_mundo(mundo: dict):
    try:
        # Conecta ao banco de dados MySQL
        # connection = mysql.connector.connect(**DB_CONFIG)
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()
        
        cursor.execute(init.USE_DATABASE)
        connection.commit()
        
        # Insere um novo mundo usando placeholders
        cursor.execute(insert.MUNDO, mundo)
        connection.commit()
        
    except Exception as e:
        print('Erro ao acessar o banco de dados:', str(e))
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com o MySQL encerrada.")

def add_salas(salas: list[dict]):
    try:
        # Conecta ao banco de dados MySQL
        # connection = mysql.connector.connect(**DB_CONFIG)
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()
        
        cursor.execute(init.USE_DATABASE)
        connection.commit()
        
        # Insere várias salas
        for sala in salas:
            cursor.execute(insert.SALA, sala)
            connection.commit()
        
    except Exception as e:
        print('Erro ao acessar o banco de dados:', str(e))
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com o MySQL encerrada.")

# Exemplo de uso
if __name__ == "__main__":
    init_db()
    
    # # Adiciona um mundo
    # mundo = {'id': 1, 'nome': 'Mundo 1'}
    # add_mundo(mundo)
    
    # # Adiciona salas
    # salas = [
    #     {'id': 1, 'nome': 'Sala 1', 'mundo_id': 1},
    #     {'id': 2, 'nome': 'Sala 2', 'mundo_id': 1}
    # ]
    # add_salas(salas)
    
    # # Obtém a quantidade de mundos
    # qtd = get_mundo_qtd()
    # print(f'Quantidade de mundos: {qtd}')