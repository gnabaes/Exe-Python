''' ATRIBUTOS DE UM ARQUIVO'''

arquivo = open('dados1.txt', 'r')

conteudo = arquivo.readline()
print('tipo de conteudo: ', type(conteudo))
print('conteudo retornado  pelo readline: ')
print(repr(conteudo))

proximo_conteudo = arquivo.readline()

print('proximo conteudo retornado: ')
print(repr(proximo_conteudo))

arquivo.close()




