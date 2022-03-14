'''  o mesmo professor  de desafio  anterior  quer  sortear o nome de um aluno para
apresentar  o trabalho dos alunos , faça um programa  que leia  o nome  dos quatro  alunos  e mostre  a ordem  sorteada
'''

import random
n1=str(input("primeiro  aluno :    "))
n2=str(input("segundo aluno:      "))
n3=str(input(" terceiro aluno:      "))
n4=str(input("quarto aluno:        "))
lista = [n1,n2,n3,n4]

#vou fazer embaralhar a lista

random.shuffle(lista)
print(" a ordem da apresentação sera:     ")
print(lista)
