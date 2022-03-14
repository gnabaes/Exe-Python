''' faça um programa que leia o comprumento do cateto oposto e catero adjacente e calculo a hipotenusa'''

CO = float(input("digite o valor de cateto oposto"))
CA = float(input("digite o comprimento do cateto adjacente"))
hi = (CO**2 + CA**2)**(1/2)

print("para cateto oposto é de{} e o cateto adjacente é de {}, o valor fa hipotenusa é {:.2f}".format(CO, CA, hi))

print("-"*12)

import math

CO1 = float(input("digite o valor do cateto oposto 1"))
CA1 = float(input("digite o valor do cateto adjacente 1"))
hi1 = math.hypot(CO1, CA1)
print("A Hipotenusa vai medir : {:.2f}".format(hi1))

print("-"*12)

from math import hypot
CO2 = float(input("digite o valor do cateto oposto 2"))
CA2 = float(input("digite o valor do cateto adjacente 2"))
hi2 = hypot(CO2, CA2)
print("o valor da hipotenusa vai ser {:.2f}".format(hi2))

