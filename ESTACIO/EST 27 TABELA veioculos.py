''' exemplo de base de dados, pessoas, marcas e veiculos'''

import sqlite3 as conector

#abertura de conexão
conexao = conector.connect("./meu_bancoRacing.db")
cursor = conexao.cursor()

#execucao de um comando:
comando = ''' CREATE TABLE Veiculo (
                    placa CHARACTER (7) NOT  NULL,
                    ano INTEGER NOT NULL,
                    cor  TEXT NOT NULL,
                    propietario INTEGER NOT NULL,
                    marca INTEGER NOT NULL,
                    PRIMARY KEY(placa),
                    FOREIGN KEY(propietario) REFERENCES pessoa(CPF),
                    FOREIGN KEY(marca) REFERENCES Marca(id)
                    );'''
cursor.execute(comando)

#efetivação do comando
conexao.commit()

#fechamento das conexões
cursor.close()
conexao.close()