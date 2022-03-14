import sqlite3 as conector

#abertura da uma conexão e aquisição de um cursor:
conexao = conector.connect("./meu_bancojaja.db")
cursor = conexao.cursor()

#execução de um comando SELECT ALTER TABLE OUTRO
comando1 = '''DROP TABLE Veiculo;'''

cursor.execute(comando1)

comando2 = '''CREATE TABLE Veiculo (
                placa CHARACTER(7) NOT NULL,
                ano  INTEGER  NOT NULL,
                cor  TEXT NOT NULL,
                motor REAL NOT NULL,
                propietario INTEGER NOT NULL,
                marca INTEGER NOT NULL,
                PRIMARY KEY (placa)
                FOREIGN KEY (propietario) REFERENCES pessoa(cpf),
                FOREIGN KEY(marca) REFERENCES marca(id)
                );'''

cursor.execute(comando2)

#efetivação  do comando
conexao.commit()

#fechamento da conexão
cursor.close()
conexao.close()

