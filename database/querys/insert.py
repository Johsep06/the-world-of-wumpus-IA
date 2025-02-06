MUNDO = '''
INSERT INTO MUNDO (ID, SIZE)
VALUES (%(id)s, %(size)s);'''

SALA = '''
INSERT INTO SALA (MUNDO_ID, POS_I, POS_J, PERCEPCAO, OBJETO)
VALUES (%(mundo_id)s, %(pos_i)s, %(pos_j)s, %(percepcao)s, %(objeto)s);'''

AGENTE = '''
INSERT INTO AGENTE(PONTOS, REGISTRO, TIPO, FINAL, HISTORICO_PASSOS, QTD_PASSOS, MUNDO_ID)
VALUES (%(pontos)s, %(registro)s, %(tipo)s, %(final)s, %(historico_passos)s, %(qtd_passos)s, %(mundo_id)s);'''