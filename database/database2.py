import psycopg2
from psycopg2.extras import execute_values
import os
from database.querys import init, insert, select

def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME", "seu_banco"),
        user=os.getenv("DB_USER", "seu_usuario"),
        password=os.getenv("DB_PASSWORD", "sua_senha"),
        host=os.getenv("DB_HOST", "localhost"),
        port=os.getenv("DB_PORT", "5432")
    )

def init_db():
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        cursor.execute(init.TABLE_MUNDO)
        cursor.execute(init.TABLE_SALA)
        cursor.execute(init.TABLE_AGENTE)
        
        connection.commit()
    except Exception as e:
        print('Erro ao criar o banco:', str(e))
    finally:
        cursor.close()
        connection.close()
        print('Conexão com o banco encerrada.')

def get_mundo_qtd() -> int:
    mundo_qtd = None
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(select.MUNDO_QTD)
        mundo_qtd = cursor.fetchone()
    except Exception as e:
        print('Erro ao acessar o banco:', str(e))
    finally:
        cursor.close()
        connection.close()
        print('Conexão com o banco encerrada.')
    
    return mundo_qtd[0] if mundo_qtd else 0

def add_mundo(mundo: dict):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        cursor.execute(insert.MUNDO, mundo)
        connection.commit()
    except Exception as e:
        print('Erro ao inserir mundo:', str(e))
    finally:
        cursor.close()
        connection.close()
        print('Conexão com o banco encerrada.')

def add_salas(salas: list[dict]):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        
        execute_values(cursor, insert.SALA, salas)
        
        connection.commit()
    except Exception as e:
        print('Erro ao inserir salas:', str(e))
    finally:
        cursor.close()
        connection.close()
        print('Conexão com o banco encerrada.')

if __name__ == '__main__':
    init_db()
    get_mundo_qtd()
