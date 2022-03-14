'''No exemplo a seguir, vamos unir os elementos de uma lista utilizando dois conectores diferentes:
o conector vírgula (‘, ‘) e o conector de nova linha (‘\n’).
Após a união, vamos gravar o conteúdo em um arquivo para mostrar o resultado '''

lista_compras = ['arroz',  'feijão',  'Erva', 'Chocolate', 'amendoin']

texto1 = ', '.join(lista_compras)
with open('texto1.txt', 'w') as arquivo:
    arquivo.write(texto1)

texto2 = '\n'.join(lista_compras)
with open('texto2.txt', 'w') as arquivo:
    arquivo.write(texto2)






