with open('texto1.txt', 'r') as arquivo:
    conteudo = arquivo.read().split(',')

with open('resultado1.txt', 'w') as resultado:
    for item in conteudo:
        texto = f'novo conteudo Antonella te amo  {item.strip()}\n'
        resultado.write(texto)
