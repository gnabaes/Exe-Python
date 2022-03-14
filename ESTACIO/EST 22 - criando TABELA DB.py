'''  criando uma tabela'''
#criando uma tabela no bando de dados

import sqlite3 as conector

conexao = None
cursor = None
try:
    #abertudra da conexão:

    conexao = conector.connect('meu_banco_Guido2021.db')
    cursor = conexao.cursor()

    #execução de um comando: SELECT, CREATE:

    comando = '''CREATE TABLE Dengue (
                codigo INTEGER NOT NULL,
                ano INTEGER NOT NULL,
                casos INTEGER NOT NULL,
                PRYMARY KEY (codigo, ano)
                );'''
    cursor.execute(comando)

    #efetivação do Comando:
    conexao.commit()

except conector.DatabaseError as erro:
    print('Erro de Banco de Dados', erro)


finally:
    #fechamento das conexões  e cursores
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()






