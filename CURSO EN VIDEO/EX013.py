#este é o execicio 15, eu pulei 2, excriva um programa de perguntas que perguntei quantos quilometros percorridos por um carro alugado  e q quantidade de dias
# pelos quais ele foi alugado. calcule o preço a pagar sabendo que o carro custa  R$ 60 e  por dia R$ 0,15 por quilometro rodado.

Kmrodados = float(input("digite quantos quilometros rodados fez o carro alugado ate hoje    Km = "))
Dias = float(input("digite o numero de dias que o carro está alugado ate hoje   dias = "))
Custo = (60*Dias + (0.15*Kmrodados))

print("o custo de aluguel do carro será de R$ {:.2f}, devido a que tem rodado {:.2f} Km e tem passado {:.2f} dias de locação".format(Custo,Kmrodados,Dias))

