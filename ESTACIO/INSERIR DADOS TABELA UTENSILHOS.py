''' INSERÇÃO DE DADOS EM TABELA '''

import sqlite3 as conector

#abertura de conexão e aquisição de cursor
conexao = conector.connect("./Cubiertos.db")
cursor = conexao.cursor()

#executar um comando: SELECT CREATE

comando = ''' INSERT INTO UTENSILHOS (Codigo, nome, Descricao, preco)
        VAlUES (10,'Faca','Faca de porcelana',50);'''

cursor.execute(comando)

#efetivação do comando
conexao.commit()

#fechamento das conexões
cursor.close()
conexao.close()