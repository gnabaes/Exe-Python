'''utilizar a palavra reservada with, disponibilizada pelo Python. Ela garante que o arquivo será fechado adequadamente após utilizarmos o arquivo, não sendo necessário chamar
o método close explicitamente.'''

print('iterando sobre o arquivo ')

with open('dados1.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)
        print('fim  do arquivo ', arquivo.name)

