''' Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.'''
nome = str(input(' digite seu nome completo por favor    ')).strip()
#print(' seu nome tem silva ?    {}'.format(nome[:5]== 'Silva'))
#preciso saber se tem silva en outra possição, suar outro operador

print(' seu nome tem silva ?    {}'.format('silva' in nome.lower()))





