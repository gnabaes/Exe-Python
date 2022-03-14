''' criando e removendo diretorios'''

import os

try:
    os.mkdir('meu diretorio')
    print('diretorio criado')
except PermissionError as erro:
    print(' sem permissão para criar diretorioas')
    print('descrição', erro)
except FileExistsError as erro:
    print('Diretorio ja existe')
    print('descrição', erro)

print('programa finalziado')

