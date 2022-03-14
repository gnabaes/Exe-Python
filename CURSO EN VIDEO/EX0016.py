#quebrando um valor,  programa que leia um numero  real e  qualquer  e mostre sua porção inteira

import math

num = float(input("digite o valor :    "))
print(" o valor digitado foi : {} e o valor da parte inteira é {} ".format(num, math.trunc(num)))


from math import trunc

num1 = float(input("digite outro valor :  "))
print("o valor digitado agora é   {} e o valor inteiro é {} ".format(num1, trunc(num1)))

num2 = float(input("digite agora outro valor por favor de novo "))
print("o resultado do valor {}, o número inteiro vai ser : {}".format(num2,int(num2)))


