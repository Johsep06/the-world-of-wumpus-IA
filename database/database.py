import sqlite3
from pathlib import Path

from database.querys import init, insert, select

ROOT_DIR = Path(__file__).parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR / DB_NAME

def init_db():
        try: 
            connection = sqlite3.connect(DB_FILE)
            cursor = connection.cursor()
            
            cursor.execute(init.TABLE_MUNDO)
            connection.commit()
            cursor.execute(init.TABLE_SALA)
            connection.commit()
            cursor.execute(init.TABLE_AGENTE)
            connection.commit()
        except Exception as e:
            print('Erro ao Criar o db', str(e))
        finally:
            connection.close()
            print('Conexão com o db encerrada.')

def get_mundo_qtd() -> int:
    mundo_qtd = None
    try:
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        cursor.execute(select.MUNDO_QTD)
        mundo_qtd = cursor.fetchone()
        
    except Exception as e:
        print('Erro ao acessar o db', str(e))
    finally:
        connection.close()
        print('Conexão com o db encerrada.')
    
    return mundo_qtd[0]

def add_mundo(mundo:dict):
        try: 
            connection = sqlite3.connect(DB_FILE)
            cursor = connection.cursor()
            cursor.execute(insert.MUNDO, mundo)
            connection.commit()
        except Exception as e:
            print('Erro ao acessar o db', str(e))
        finally: 
            connection.close()
            print('Conexão com o db encerrada.')

def add_salas(salas:list[dict]):
    try: 
        connection = sqlite3.connect(DB_FILE)
        cursor = connection.cursor()
        
        for sala in salas:
            cursor.execute(insert.SALA, sala)
            connection.commit()
    except Exception as e:
        print('Erro ao acessar o db', str(e))
    finally: 
        connection.close()
        print('Conexão com o db encerrada.')

if __name__ == '__main__':
    init_db()
    get_mundo_qtd()