''' banco de dados '''

import sqlite3 as conector

#abertura de conexão sive para conectar com um banco de dados
conexao= conector.connect('URL SQLite.db')

#aquisição  de um cursor
cursor = conexao.cursor()

#Executando Comandos SELECT e CREATE
cursor.execute("""
CREATE TABLE clientes (
    id INTEGER NOT NULL PRIMARY  KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER,
    cpf         VARCHAR(11) NOT null,
    email  TEXT  NOT NULL,
    fone TEXT,
    cidade TEXT
    uf VARCHAR(2) NOT NULL,
    criado_em DATE NOT NULL
);"""
)

cursor.fetchall()

#Efetivação de Comando
conexao.commit()

#fechamento das conexoes com um banco de dados
cursor.close()
conexao.close()

