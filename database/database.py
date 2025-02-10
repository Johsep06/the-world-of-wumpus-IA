# import mysql.connector
import pymysql
from pathlib import Path
from dotenv import load_dotenv # type:ignore
import os

from database.querys import init, insert, select
# from database.config_db import DB_CONFIG # Dicionario com as Configuações do MySQL

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# Configurações do banco de dados
DB_CONFIG = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'port': int(os.getenv('DB_PORT'))
}

def init_db():
    connection = None
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
    connection = None
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

def get_agente_qtd() -> int:
    agente_qtd = None
    connection = None
    try:
        # Conecta ao banco de dados MySQL
        # connection = mysql.connector.connect(**DB_CONFIG)
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()
        
        cursor.execute(init.USE_DATABASE)
        connection.commit()
        
        # Executa a consulta para obter a quantidade de Agentes
        cursor.execute(select.AGENTE_QTD)
        agente_qtd = cursor.fetchone()
        
    except Exception as e:
        print('Erro ao acessar o banco de dados:', str(e))
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com o MySQL encerrada.")
    
    return agente_qtd[0] if agente_qtd else 0

def save_mundo(mundo: dict):
    connection = None
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

def save_agente(agente: dict):
    connection = None
    try:
        # Conecta ao banco de dados MySQL
        # connection = mysql.connector.connect(**DB_CONFIG)
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()
        
        cursor.execute(init.USE_DATABASE)
        connection.commit()
        
        # Insere um novo mundo usando placeholders
        cursor.execute(insert.AGENTE, agente)
        connection.commit()
        
    except Exception as e:
        print('Erro ao acessar o banco de dados:', str(e))
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com o MySQL encerrada.")

def save_salas(salas: list[dict]):
    connection = None
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

def get_mundo(mundo_id:int):
    mundo = None
    salas = None
    connection = None
    try:
        # Conecta ao banco de dados MySQL
        # connection = mysql.connector.connect(**DB_CONFIG)
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()
        
        cursor.execute(init.USE_DATABASE)
        connection.commit()
        
        # Executa a consulta para obter a quantidade de mundos
        param = {'mundo_id':mundo_id}
        cursor.execute(select.MUNDO_BY_ID, param)
        mundo = cursor.fetchone()
        
        
        cursor.execute(select.SALA, param)
        salas = cursor.fetchall()
        
    except Exception as e:
        print('Erro ao acessar o banco de dados:', str(e))
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com o MySQL encerrada.")
    
    return {
        'id':mundo[0],
        'size':mundo[1],
        'salas':salas
    }

# Exemplo de uso
if __name__ == "__main__":
    init_db()