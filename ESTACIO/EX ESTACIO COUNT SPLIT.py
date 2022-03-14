#função count

print('-'*60)

with open('dados1.txt', 'r') as arquivo:
    texto = arquivo.read()
    contador = texto.count('ola')

    print('total de Olas = ', contador)

    #função SPLIT (quebra)

frase1 = 'Eu amo comer amoras no cafe da manhã'
lista_termos1 = frase1.split()
print(lista_termos1)

print('-'*50 )

frase2 = ' Amora  Abacaxi  Abacati   Banana'
lista_termos2 = frase2.split()
print(lista_termos2)

print('-'*50)

frase3 = 'Carro, Moto, Avião'
lista_termos3 = frase3.split()
print(lista_termos3)


print('-'*60)
''' O método split é utilizado para quebrar uma string em uma lista de palavras. 
O parâmetro passado para esse método é utilizado como separador.
 Ao executar o comando frase.split(“;”), criamos a lista [“Ômega”, “Opala”, “Monza”].'''

frase4 = 'Omega;Opala;Monza'
lista_frase4 = frase4.split(';')
print(lista_frase4)

