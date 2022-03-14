''' 027: Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e o último nome separadamente.'''

nome = str(input(' Digite seu nome completo para fazer analise:  ')).strip()
n = nome.split()
print('seu primeiro nome é {}'.format( n[0]))
print(' seu último  nome é {}'.format(n[len(n)-1]))
# se usar a função len, va me disser quantos nomes tem em total como o python trabalha desde a posição zero, temos
#que colocar o menos 1 se duvidas ler aula 9 do curso em Video









