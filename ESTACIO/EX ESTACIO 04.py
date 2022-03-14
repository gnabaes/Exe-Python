''' ATRIBUTOS DE UM ARQUIVO'''

arquivo = open('dados1.txt', 'r')
conteudo = arquivo.read()
print('tipo de conteudo: ', type(conteudo))
print('conteudo retornado pelo read')
print('-'*40)
print(repr(conteudo))
arquivo.close()

