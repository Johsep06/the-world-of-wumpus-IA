MUNDO = '''
INSERT INTO MUNDO (ID, TAMANHO)
VALUES (%(id)s, %(tamanho)s);'''

AGENTE = '''
INSERT INTO AGENTE(ID, TIPO)
VALUES (%(id)s, %(tipo)s);'''

MEMORIA = '''
INSERT INTO MEMORIA (ID)
VALUES (%(id)s);'''

SALA = '''
INSERT INTO SALA (MUNDO_ID, POS_X, POS_Y, POS_Z, PERCEPCAO, OBJETO)
VALUES (%(mundo_id)s, %(pos_x)s, %(pos_y)s, %(pos_z)s, %(percepcao)s, %(objeto)s);'''

CELULA = '''
INSERT INTO CELULA (MEMORIA_ID, POS_X, POS_Y, POS_Z, CONTEUDO)
VALUES (%(memoria_id)s, %(pos_x)s, %(pos_y)s, %(pos_z)s, %(conteudo)s);'''

EXPLORACAO = '''
INSERT INTO EXPLORACAO
(
        REGISTRO, MUNDO_ID, AGENTE_ID, MEMORIA_ID, 
        RESULTADO, FLECHAS_USADAS, PONTOS, HISTORICO_DE_ACOES, 
        QTD_PASSOS, QTD_OUROS_COLETADOS, QTD_WUMPUS_VENCIDOS)
VALUES 
(
        %(registro)s, %(mundo_id)s), %(agente_id)s), %(memoria_id)s), 
        %(resultado)s), %(flechas_usadas)s, %(pontos)s, %(historico_de_acoes)s, 
        %(qtd_passos)s,%(qtd_ouros_coletados)s, %(qtd_wumpus_vencidos)s,
);'''

BASEADA = '''
INSERT INTO BASEADA (REGISTRO, MUNDO_ID, MEMORIA_ID)
VALUES (%(registro)s, %(mundo_id)s, %(memoria_id)s);
'''