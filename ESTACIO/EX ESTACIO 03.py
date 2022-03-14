'''ATRIBUTOS DE UM ARQUIVO'''

arquivo = open('dados1.txt','r')

print('nome do arquivo: ', arquivo.name)
print('modo do arquivo: ', arquivo.mode)
print('Arquivo Fechado', arquivo.closed)

arquivo.close()

print('arquivo fechado ', arquivo.closed)
