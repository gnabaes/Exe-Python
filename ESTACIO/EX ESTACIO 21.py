''' usar scandir para listado de diretorios'''

import os

try:
    entradas = os.scandir('meu diretorio')

    for obj in entradas:
        print(obj)
        print('Nome: ', obj.name)
        print('caminho: ', obj.path)
        print(' E diretorio: ', obj.is_dir())
        print(' E arquivo: ', obj.is_file())
        if obj.is_file():
            print("tamanho:   ", obj.start().st_size, "B")
            print('-'*60)

except FileNotFoundError:
    print(' o caminho  não existe')
except NotADirectoryError:
    print('o caminho não é de um diretorio')

print('programa terminado')

