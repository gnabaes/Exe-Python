''' Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".'''

cid= str(input('em que cidade vc naceu ?   ')).strip()
print(cid[:5].upper()== 'SANTO')  # foi colocado upper para evitar o usuario se colocar com minuscula ou maiuscula desta formar transforma todo maiusculo evita erro




