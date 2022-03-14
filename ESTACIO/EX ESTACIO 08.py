''' Fechar e abrir novamente o arquivo. Utilizar o método seek(n), passando como argumento o número
 da linha onde desejamos posicionar o cursor. A chamada seek(0) retorna o cursor para o início do arquivo.'''

arquivo = open('dados1.txt', 'r')
conteudo = arquivo.read()
print('todo o conteúdo  do arquivo')
print(repr(conteudo), '\n')

print('-'*50)

conteudo_leitura = arquivo.read()
print('releitura de todo  o conteudo  do arquivo')
print(repr(conteudo_leitura),'\n')

arquivo.close()

print('-'*50)

arquivo_reaberto = open('dados1.txt', 'r')
conteudo_reaberto = arquivo_reaberto.read()
print(' todo conteudo  do arquivo  novamente : ')
print(repr(conteudo_reaberto), '\n')

print('-'*50)

arquivo_reaberto.seek(0)
conteudo_seek = arquivo_reaberto.read()
print('todo o conteudo  do arquivo  apos  o SEEK')
print(repr(conteudo_seek))

arquivo_reaberto.close()


