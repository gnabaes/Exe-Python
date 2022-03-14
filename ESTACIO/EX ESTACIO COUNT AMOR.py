
frase = 'Eu amo comer amoras no cafe da manhã '

#resultado obtido utilizando o metedo COUNT

print('contagem da palavra Amo: ', frase.count('amo'))

print('-'*50)

#resultado obtido usando metodo  split

contador = 0
lista_termos = frase.split()
for termo in lista_termos:
    if termo == 'amo':
        contador += 1
print('contagem da palavra amo: ', contador)

