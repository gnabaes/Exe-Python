''' ITERAR NA VARIAVEL ARQUIVO'''

arquivo = open('dados1.txt')

print('iterando sob o arquivo')
for linha in arquivo:
    print(repr(linha))

print('-'*50)

arquivo.close()

#Na linha 4, utilizamos o laço for para iterar diretamente sobre a variável arquivo.
# Para cada iteração, recebemos uma nova linha do arquivo, disponibilizada na variável linha,
# impressa na linha 5. Observe a saída do console abaixo da figura.