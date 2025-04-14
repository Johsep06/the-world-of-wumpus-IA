# import mysql.connector
import pymysql
from pathlib import Path
from dotenv import load_dotenv 
import os

from database.querys import init, insert, select

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv(override=True)

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
        cursor.execute(init.USE_DATABASE)
        cursor.execute(init.TABLE_MUNDO)
        cursor.execute(init.TABLE_AGENTE)
        cursor.execute(init.TABLE_MEMORIA)
        cursor.execute(init.TABLE_SALA)
        cursor.execute(init.TABLE_CELULA)
        cursor.execute(init.TABLE_EXECUCAO)
        connection.commit()
    except Exception as e:
        print('Erro ao criar o banco de dados:', str(e))
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com o MySQL encerrada.")

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

def save_memoria(memoria: dict):
    connection = None
    try:
        # Conecta ao banco de dados MySQL
        # connection = mysql.connector.connect(**DB_CONFIG)
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()
        
        cursor.execute(init.USE_DATABASE)
        connection.commit()
        
        # Insere um novo mundo usando placeholders
        cursor.execute(insert.MEMORIA, memoria)
        connection.commit()
        
    except Exception as e:
        print('Erro ao acessar o banco de dados:', str(e))
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com o MySQL encerrada.")

def save_celulas(celulas: list[dict]):
    connection = None
    try:
        # Conecta ao banco de dados MySQL
        # connection = mysql.connector.connect(**DB_CONFIG)
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()
        
        cursor.execute(init.USE_DATABASE)
        connection.commit()
        
        # Insere várias salas
        for celula in celulas:
            cursor.execute(insert.CELULA, celula)
            connection.commit()
        
    except Exception as e:
        print('Erro ao acessar o banco de dados:', str(e))
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com o MySQL encerrada.")

def save_baseada(baseada: dict):
    connection = None
    try:
        # Conecta ao banco de dados MySQL
        # connection = mysql.connector.connect(**DB_CONFIG)
        connection = pymysql.connect(**DB_CONFIG)
        cursor = connection.cursor()
        
        cursor.execute(init.USE_DATABASE)
        connection.commit()
        
        # Insere um novo mundo usando placeholders
        cursor.execute(insert.BASEADA, baseada)
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
        
        param['mundo_id'] = mundo[2].strftime('%Y-%m-%d %H:%M:%S')
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

def get_all_worlds():
    dados = []
    mundos = None
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
        cursor.execute(select.MUNDO)
        mundos = cursor.fetchall()
        
        for mundo in mundos:
            param = {'mundo_id':mundo[2].strftime('%Y-%m-%d %H:%M:%S')}
            cursor.execute(select.SALA, param)
            salas = cursor.fetchall()
            dados.append ({
                'id':mundo[0], 
                'tamanho':mundo[1], 
                'registro':param['mundo_id'],
                'salas':salas
            })
        
        
        # cursor.execute(select.SALA)
        # salas = cursor.fetchall()
        
    except Exception as e:
        print('Erro ao acessar o banco de dados:', str(e))
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Conexão com o MySQL encerrada.")
    
    return dados

# Exemplo de uso
if __name__ == "__main__":
    init_db()