''' Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas'''

v = float(input('para saber se sua viagem é longa ou não precisso que e informe os KM de distancia por favor, \n : '))
if v <= 200:
    preço = v*0.5
    print(" sua viagem é curta e o preço dela é   {} reais ".format((preço)))
else:
    preço = v * 0.45
    print('digite que seua viage é longa e o seru preço vai ser  {}'.format(preço))

# ou podemos escrever em forma simples preço = v*0.5 if v <=200 else v*0,45