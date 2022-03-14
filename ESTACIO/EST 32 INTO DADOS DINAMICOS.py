''' inserir dados em tabela com queries dinâmicas'''
import sqlite3 as conector

class pessoa:
    def cpf(self, cpf):
        self.cpf = cpf
    def nome(self,nome):
        self.nome = nome
    def data_nascimento(self,data_nascimento):
        self.data_nascimento = data_nascimento
    def usa_oculos(self, usa_oculos):
        self.usa_oculos = usa_oculos

#abertura de conexao e aquisição de cursor
conexao = conector.connect('./meu_bancoRacing.db')
cursor = conexao.cursor()

#criação de um objeto de tipo Pessoa
pessoa1 = pessoa(12345678910, 'Mario', '2000-01-31', True)

#definição de um comando com query parameter
comando = ''' INSERT INTO Pessoa (cpf, nome, nascimento, oculos)
                    VALUES (:cpf, :nome,:data_nascimento,:usa_oculos);'''
cursor.execute(comando, {"cpf": pessoa1.cpf,
                         "nome": pessoa1.nome,
                         "data_nasimento": pessoa1.data_nascimento,
                         "usa_oculos": pessoa1.usa_oculos})

#efetivação do omando
conexao.commit()

#fechamento das conexões
cursor.close()
conexao.close()

