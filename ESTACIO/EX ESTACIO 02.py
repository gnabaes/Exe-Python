''' para abrir arquivo absoluto ou relativos'''

import os

arquivo1 = open("dados1.txt") #caminho relativo
arquivo2 = open('C:\\Users\\Bolivarense\\Documents\\06 - CURSOS\\Curso 2020\\CURSO ADS ESTACIO\\2A1S PYTHON\\Tema 3 - Python estruturado - arquivos py\\EXERCICIOS\\dados1.txt')

print('-'*50)
print(os.path.relpath(arquivo1.name))
print('-'*50)
print(os.path.abspath(arquivo1.name))
print('-'*50)
print(arquivo1)
print('-'*50)
print(os.path.relpath(arquivo2.name))
print('-'*50)
print(os.path.abspath(arquivo2.name))
print('-'*50)
print(arquivo2)
