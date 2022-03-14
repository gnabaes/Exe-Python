''' ATRIBUTOS DE UM ARQUIVO'''

arquivo = open('dados1.txt', 'r')
conteudo = arquivo.readlines()
print('tipo  de conteudo, ', type (conteudo))

print('conteudo retornado pelo realines:  ')
print(repr(conteudo))

arquivo.close()

