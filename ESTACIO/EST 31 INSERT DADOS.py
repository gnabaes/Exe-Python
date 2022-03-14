''' INSERÇÃO DE DADOS EM TABELA '''

import sqlite3 as conector

#abertura de conexão e aquisição de cursor
conexao = conector.connect("./meu_bancoRacing.db")
cursor = conexao.cursor()

#executar um comando: SELECT CREATE

comando = ''' INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
        VAlUES (12345678910, 'Mario', '2000-01-31', true);'''

cursor.execute(comando)

#efetivação do comando
conexao.commit()

#fechamento das conexões
cursor.close()
conexao.close()

