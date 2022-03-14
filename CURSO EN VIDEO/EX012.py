#faça um algoritmo que leia o preço de um produto e calculo o novo preço com aumento de 5 %

P1=float(input("digite o prçeo do produto por favor  R$    "))
A1 = float(input("digite o percentual de aumento do preço  %"))

NP1 = P1*(1+A1/100)

print("para o valor atual do produtor {:.2f} e um aumento de preço de {:.2f} % o novo valor do produto será de R$ {:.2f}".format(P1,A1,NP1))

