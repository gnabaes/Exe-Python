''' erros e exeções '''

print('abrindo um arquivo')

try:
    open('guido.txt', 'r')
    print('arquivo aberto')
except FileNotFoundError as erro:
    print('Arquivo inexistente')
    print('Descrição ', erro)

print('termino do programa')








