MUNDO = '''
INSERT INTO MUNDO (TAMANHO, REGISTRO)
VALUES (%(tamanho)s, %(registro)s);'''

AGENTE = '''
INSERT INTO AGENTE(TIPO, REGISTRO)
VALUES (%(tipo)s, %(registro)s);'''

MEMORIA = '''
INSERT INTO MEMORIA (MUNDO_ID, REGISTRO)
VALUES (%(mundo_id)s, %(registro)s);'''

SALA = '''
INSERT INTO SALA (MUNDO_ID, POS_X, POS_Y, POS_Z, PERCEPCAO, OBJETO)
VALUES (%(mundo_id)s, %(pos_x)s, %(pos_y)s, %(pos_z)s, %(percepcao)s, %(objeto)s);'''

CELULA = '''
INSERT INTO CELULA (MEMORIA_ID, POS_X, POS_Y, POS_Z, CONTEUDO)
VALUES (%(memoria_id)s, %(pos_x)s, %(pos_y)s, %(pos_z)s, %(conteudo)s);'''

EXECUCAO = '''
INSERT INTO EXECUCAO
(
        REGISTRO, MUNDO_ID, AGENTE_ID, MEMORIA_ID, 
        RESULTADO, HISTORICO_DE_ACOES, FLECHAS_USADAS, PONTOS, 
        QTD_PASSOS, QTD_OUROS_COLETADOS, QTD_WUMPUS_VENCIDOS)
VALUES 
(
        %(registro)s, %(mundo_id)s), %(agente_id)s), %(memoria_id)s), 
        %(resultado)s), %(historico_de_acoes)s, %(flechas_usadas)s, %(pontos)s, 
        %(qtd_passos)s,%(qtd_ouros_coletados)s, %(qtd_wumpus_vencidos)s,
);'''