''' simulado SELECT'''

import sqlite3 as conector

#abertura de conexão  e aquisição  de cursor
conexao = conector.connect("./Cubiertos.db")
cursor = conexao.cursor()

#execucao de um comando:
comando = ''' CREATE TABLE UTENSILHOS (
                    Codigo CHARACTER (2) NOT  NULL,
                    nome INTEGER NOT NULL,
                    Descricao  TEXT NOT NULL,
                    preco INTEGER NOT NULL,
                    PRIMARY KEY(Codigo)
                    );'''


cursor.execute(comando)

#efetivação do comando
conexao.commit()

#fechamento das conexões
cursor.close()
conexao.close()


