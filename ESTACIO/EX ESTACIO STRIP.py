
with open('dados1.txt', 'r') as arquivo:
    print('representação  original  da linha')
    for linha in arquivo:
        print(repr(linha))

print('-'*60)

with open('dados1.txt', 'r') as arquivo:
    print('representação  original  da linha apos strip')
    for linha in arquivo:
        linha_limpa = linha.strip()
        print(repr(linha_limpa))

#idem acima agora inserindo um contador de linhas






