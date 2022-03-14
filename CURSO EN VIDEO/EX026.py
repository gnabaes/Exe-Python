''' 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
 em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.'''

frase = str(input(' digite uma frase por favor para contar quantas vezes aparece a letra A  ')).strip().upper()
print(' a letra A aparece   {} vezes na frase'.format(frase.count('A')))
print(' a primeira letra A aparece na possição   {}'.format(frase.find('A')+1))
print(' a utlima letra A apaece na posição   {}'.format(frase.rfind('A')+1))

# foi corrigido o contador + 1 porque sabemos que o python conta dese o 0
# foi usado o rfind  para procurar a contar desde a direita a quantidade de carateres e procura a primeira isso foi usado par achar a ultima letra A




