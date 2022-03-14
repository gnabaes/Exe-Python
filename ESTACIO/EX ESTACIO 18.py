''' uso da função renome'''

import os

try:
    os.rename('dados_write.txt', 'dados_Escritos.txt')
    print('arquivo renomeado !')
except FileNotFoundError as erro:
    print('arquivo  inexistente')
    print('descrição', erro)
except PermissionError as erro:
    print('arquivo ja aberto por outro programa')
    print('descrição', erro)
except FileExistsError as erro:
    print('arquivo destino ja existe')
    print('descrição', erro)
print('programa terminado')

