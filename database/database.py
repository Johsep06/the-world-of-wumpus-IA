import sqlite3
from pathlib import Path

from querys import init

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
            
if __name__ == '__main__':
    init_db()