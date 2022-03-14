''' Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.'''

num = int(input(' digite um numero inteiro de 0 a 9999 : '))
n = str(num)
u = num // 1 % 10
d = num//10 % 10
c = num //100 % 10
m = num //1000 % 10

print('analisando o numero  {}'.format(num))
print('a unidade deste número é  {}'.format(n[3]))
print(' a decena vai ser o número {}'.format(n[2]))
print('a centena vai ser o número  {}'.format(n[1]))
print(' o milhar vai ser o número  {}'.format(n[0]))

# temos que corrgir o erro quando digitar apenas tre ores o meons numeros
