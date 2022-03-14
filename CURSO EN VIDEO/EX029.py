''' Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
 mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite'''
v1 = int(input('o Radar pegou sua velocidade do seu carro, favor digitar:  '))
if v1 >80:
    m1 = 7 * (v1 - 80)
    print('Sua velocidade está acima da permitida e será multado')
    print("o valor da multa vai ser  {}  reais ".format(m1))
else:
    print('tenha um bom dia e continue dirigindo com segurança')
