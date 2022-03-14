''' continua exemplo de remover diretorios'''

import os

try:
    os.rmdir('meu diretorio')
    print('Diretorio removido !!')
except PermissionError as erro:
    print(' sem permissão para  remover diretorio')
    print('descrição', erro)
except FileNotFoundError as erro:
    print('diretorio inesxistente ')
    print(' descrição', erro)
except OSError as erro:
    print('Outro erro.')
    print('descrição', erro)

print("programa finalizado com sucesso !!!!")
