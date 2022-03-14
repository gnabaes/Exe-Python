''' programa para analisar o texto digitado e mostre o nome com todas as letras maiusculs, minuculas, contar quantas
letras ao todo e  quantas letras tem  o primeiro nome'''

nome = str(input('digite seu nome completo por favor:      ')).strip()   # digitar string pra explicitar que vai ser um string e colocamos strip para eliminar os espaço antes e depois
print('analisando seu nome:  .....')
print('seu nome em letras maiusculas é :  {}'.format(nome.upper()))
print(' seu nome em letras minusculas é :   {}'.format(nome.lower()))
print(' seu nome em letras Capitalizado é :   {}'.format(nome.capitalize()))
print('seu nome em total tem:  {}'.format(len(nome) - nome.count(' '))) #tambem para eliminar os espaço entre letras usar nome.count( )

#print('seu  primeiro nome tem   {}  letras aqui'.format(nome.find(' ')))   colocado # para dar otra forma de fazer o mesmo abaixo separando os nomes
separa = nome.split()
print('seu primeiro nome é:   {} e ele tem {} letras'.format(separa[0],len(separa[0])))
