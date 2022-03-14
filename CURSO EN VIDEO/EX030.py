'''  Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.'''

n1 = int(input('digite um numero inteiro para analise se o numero é impar ou par por favor,\n  :  '))
print('-*'*30)
r1 = n1 % 2
if r1 >0:
    print('seu numero é IMPAR por que o resto da divisão é {}'.format(r1))
else:
    print('o resultado da analise é PAR, porque o resultado do resto é {}'.format(r1))



