#quanto dinheiro tem na sua carteira e converta em Dolares

dinheiro = float(input("digete quanto dinhero quer convertir para dolares  R$  "))
Cotacaodolar = float(input("digite a cotação do dolar de hoje "))
Dolares = float(dinheiro/Cotacaodolar)  #os numeros decimais trabalhar com ponto e não com virgula
print("o dinheiro que vc tem na carteira R$ {:.2f} pode comprar U$S {:.2f}".format(dinheiro, Dolares))



