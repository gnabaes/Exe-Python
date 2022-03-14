'''Ano Bissexto'''
from  datetime import date
ano = int(input('didite o que ano quere analisar ? se o ano for o atual digite o 0  \n   : '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or  ano % 400 == 0:
    print(' o ano {}  é BISEXTO'.format(ano))
else:
    print('o ano  {} NÂO é BISEXTO'.format(ano))

