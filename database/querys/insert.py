MUNDO = '''
INSERT INTO MUNDO (ID, SIZE)
VALUES (:id, :size);'''

SALA = '''
INSERT INTO SALA (MUNDO_ID, POS_I, POS_J, PERCEPCAO, OBJETO)
VALUES (:mundo_id, :pos_i, :pos_j, :percepcao, :objeto);'''

AGENTE = '''
INSERT INTO AGENTE(PONTOS, REGISTRO, TIPO, FINAL, HISTORICO_PASSOS, QTD_PASSOS, MUNDO_ID)
VALUES (:pontos, :registro, :tipo, :final, :historico_passos, :qtd_passos, :mundo_id);'''