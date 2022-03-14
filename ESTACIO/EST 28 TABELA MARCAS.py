''' exemplo de base de dados, pessoas, marcas e veiculos'''

import sqlite3 as conector

#abertura de conexão
conexao = conector.connect("./meu_bancoRacing.db")
cursor = conexao.cursor()

#execucao de um comando:
comando = ''' CREATE TABLE Marca (
                    id INTEGER NOT  NULL,
                    nome TEXT NOT NULL,
                    sigla CHARACTER(2) NOT NULL,
                    PRIMARY KEY (id)
                    );'''

cursor.execute(comando)

#efetivação do comando
conexao.commit()

#fechamento das conexões
cursor.close()
conexao.close()