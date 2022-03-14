''' alterar dados de uma tabela ja existente'''

import sqlite3 as  conector

#abertura de conexão  e aquisição  de cursor
conexao = conector.connect("./meu_bancoRacing.db")
cursor = conexao.cursor()

#execução de um comando SELEC CREATE ......
comando = '''ALTER TABLE  Veiculo 
                ADD motor  REAL;'''

cursor.execute(comando)

#efetivação do comando
conexao.commit()

#fechamento das conexoes
cursor.close()
conexao.close()
