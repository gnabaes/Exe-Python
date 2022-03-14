#faça um programa que leia algo pelo teclado e mostre na tela o seu  tipo primitivo e todas as informações possiveis  sobre ela

b = input("digite algo   ")
print(" o tipo primitivo  desse valor é:  ", type(b))
print("so tem  espaços?", b.isspace())
print(" é um número ? ",b.isnumeric())
print(" é um alfabeto ?", b.isalpha())
print(" é um alfanúmerico ? ", b.isalnum())
print("é letra maiuscula ?", b.isupper())
print(" é letra minuscula ?", b.islower())
print(" está capitalizada ?", b.istitle())
print("está informação digitada é o tipo primitivo  desse valor é:{},espaços: {}, é um número: {}, é um alfabeto: {},é um alfanúmerico {}, é letra maiuscula {},é letra minuscula {} e está capitalizada {}".format(type(b),b.isspace(),b.isnumeric(),b.isalpha(),b.isalnum(),b.isupper(),b.islower(),b.istitle()))
