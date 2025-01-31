MUNDO = '''
INSERT INTO MUNDO (SIZE)
VALUES (:size);'''

SALA = '''
INSERT INTO SALA (MUNDO_ID, POS_X, POS_Y, PERCEPCAO, OBJETO)
VALUES (:mundo_id, :pos_x, :pos_y, :percepcao, :objeto);'''

AGENTE = '''
INSERT INTO AGENTE(PONTOS, REGISTRO, TIPO, FINAL, HISTORICO_PASSOS, QTD_PASSOS, MUNDO_ID)
VALUES (:pontos, :registro, :tipo, :final, :historico_passos, :qtd_passos, :mundo_id);'''