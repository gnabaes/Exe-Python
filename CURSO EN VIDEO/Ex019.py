''' exemplo 19 de curso em vidio https://www.youtube.com/watch?v=_Nk02-mfB5I  um professor que sortear um
dos seus 4 alunos  para apagar o quadro . faça um programa  que ajude  ele,  lendo o nome deles
e escrevendo o nome do escolhido '''

import random

n1 = str(input("primeiro aluno:    "))
n2 = str(input("segundo aluno:      "))
n3 = str(input("terceiro aluno:     "))
n4 = str(input("quart aluno:        "))
Lista = [n1,n2,n3,n4]
escolhido = random.choice(Lista)

print("  o aluno escolhido  foi {}".format(escolhido))


