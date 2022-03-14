#vamos utilizar operadores aritmeticos, criar um algoritmo que leia um numero e mostre dobro, triplo e raiz quadrada

n =int(input("digitar um número   "))

d = n * 2
t = n * 3
r = n ** (1/2)   # tambem podemos escrever como potencia pow(base, potencia)
r = pow(n,(1/2))

print("o numero digitao é {}, \n o resultado do dobro é {}, \n  o resultado do triplo é {}, \n o resultado da Raiz quadrada é {}".format(n,d,t,r))

