''' uso da função remover'''
import os
try:
    os.remove('dados1.txt')
    print('arquivo removido !')

except FileNotFoundError as erro:
    print('arquivo inexistente')
    print('Descrição do Erro: ', erro)

except permissionError as erro:
    print('sem  permissão  para acessar o arquivo')
    print('descrição do erro', erro)

print('termino do programa')

