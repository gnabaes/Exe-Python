''' exemplo de uma base de dados taxa de contagios de dengue no rio de janeiro
Taxa de incidencia =  numero de novos casos / numero de pessoas em risco
1) criar um banco de dados das informações de dengue para armazenar as informaçoes sobre os
casos de dengue e população
2) Criar um modelo  ER e as Tabelas
3) Povoar o banco de dados a partir de planilhas contendo  casos  de dengue  e população
4) consultar o banco de dados e obter a taxa de incidencia'''

#fonte de informaçãoes necessarias
# Casos de Dengue DATASUS e População IBGE

import sqlite3 as conector

conexao = None
cursor = None
try:
    conexao = conector.connect('meu_banco_novo2.db')
    conexao.execute('PRAGMA foreign_keys = on')
    cursor = conexao.cursor()

    comando = """ CREATE TABLE Municipio (
                codigo INTEGER NOT NULL,
                nome VARCHAR(32) NOT NULL,
                PRIMARY KEY (codigo)
                );"""
    cursor.execute(comando)

    comando = """ CREATE TABLE Populacao (
                codigo INTEGER NOT NULL,
                ano INTEGER NOT NULL,
                PRIMARY KEY (codigo, ano),
                FOREIGN KEY(codigo) REFERENCES Municipio(codigo)
                );"""
    cursor.execute(comando)

    comando = """ CREATE TABLE Dengue (
                codigo INTEGER NOT NULL,
                ano INTEGER NOT NULL,
                casos INTEGER NOT NULL,
                PRIMARY KEY (codigo, ano)
                FOREIGN KEY (codigo) REFERENCES Municipio(codigo)
                );"""
    cursor.execute(comando)

    conexao.commit()

except conector.DatabaseError as erro:
    print('Erro de Banco de Dados', erro)

finally:
    #fechamento das conexões  e cursores
    if cursor:
        cursor.close()
    if conexao:
        conexao.close()

