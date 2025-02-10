MUNDO = '''
INSERT INTO MUNDO (ID, SIZE)
VALUES (%(id)s, %(size)s);'''

SALA = '''
INSERT INTO SALA (MUNDO_ID, POS_I, POS_J, PERCEPCAO, OBJETO)
VALUES (%(mundo_id)s, %(pos_i)s, %(pos_j)s, %(percepcao)s, %(objeto)s);'''

AGENTE = '''
INSERT INTO AGENTE(ID, PONTOS, FLECHAS, REGISTRO, TIPO, FINAL, HISTORICO_PASSOS, QTD_PASSOS, WUMPUS, MUNDO_ID)
VALUES (
        %(id)s, 
        %(pontos)s, 
        %(flechas)s, 
        %(registro)s, 
        %(tipo)s, 
        %(final)s, 
        %(historico_passos)s, 
        %(qtd_passos)s,
        %(wumpus)s,
        %(mundo_id)s);'''