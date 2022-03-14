''' exemplo de base de dados, pessoas, marcas e veiculos'''

import sqlite3 as conector

try:
    #abertura de conexão
    conexao = conector.connect("./meu_bancoRacing.db")
    cursor = conexao.cursor()

    #execucao de um comando:
    comando = ''' CREATE TABLE Pessoa (
                    cpf INTEGER NOT  NULL,
                    nome TEXT NOT NULL,
                    nascimento DATE NOT NULL,
                    oculos BOOLEAN NOT NULL,
                    PRIMARY KEY(cpf));'''
    cursor.execute(comando)

    #efetivação do comando
    conexao.commit()

except conector.DatabaseError as err:
    print("erro  de bando de dados", err)

finally:
    #fechamento das conexoes
    if conexao:
        cursor.close()
        conexao.close()

