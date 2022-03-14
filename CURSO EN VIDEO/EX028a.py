'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido
pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.'''

from random import randint
from time import sleep
computador = randint(0,5)  # faz o compurador sortear
print(' vou pensar em um numero entre 0 e 5 tente adivinhar ?')
print('-'*20)
j1 = int(input('por favor digite um numero que eu estou pensando ?'))
print('Processando .....')
sleep (3)
if j1 == computador:
    print('PARABENS VOCE ACERTOU !!! voce disse o número {} e eu pendei no {}'.format(j1,computador))
else:
    print("VOCE PERDEU porque não acertou !! voce disse o numero {} e eu pensei {}".format(j1,computador))
