#pintura de uma parede, para calcula area da parede, sua parede tem  2.5 x  1.75  e sua area  é de 4.375 m2.
#para pintar a parede quantos litros de tinta ? se o rendimento é de 1 litro cada 2 metros quadrados.

largura_pared = float(input("digite a largura da parede "))
altura_pared = float(input("digite altura da parede "))
rendimento_tinta = float(input('digite o rendimento por litro da tinta'))

area_pared = largura_pared * altura_pared
#rendimento da 1 litro de tinta é de 2 m2

tinta = (area_pared / rendimento_tinta)

print("para uma parede de largura {:.2f} e altura {:.2f}, tem uma área de {:.2f}, é necessario {:.2f}  litros de tinta".format(largura_pared,altura_pared, area_pared, tinta))
