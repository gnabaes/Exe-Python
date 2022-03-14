''' formatação de string utilizando f-string, como a definição de largura de uma string, formatação de float e de datas.'''

from datetime import datetime

frutas = ['jabuticaba', 'laranja', 'Uva',  'Banana']
for fruta in frutas:
    minha_fruta = f'nome:   {fruta:12} - numero de letras: {len(fruta):3}' # 12 e o 3 são numeros de espaço
    print(minha_fruta)
print()

pi = 3.1415
meu_numero = f'O numero  PI é : {pi:.1f}'
meu_numero_deslocadao = f' o meu numero deslocadao é {pi:6.1f}'  # o numero 6 é largura e o numero depois do ponto é a presição
meu_numero_maispreciso = f' o numero PI masi preciso é: {pi:.4f}'
print(meu_numero)
print(meu_numero_maispreciso)
print(meu_numero_deslocadao)

print()

data = datetime.now()
minha_data = f'a data de hoje é  {data}'
minha_dataformatada = f'a data formatada é {data:%d/%m/%y}' #ue indica que desejamos exibir a data no formato “dia/mês/ano”
print(minha_data)
print(minha_dataformatada)

