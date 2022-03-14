#digite uma distancia em metros e me retorne a conversão de unidade em Km, hm, DCam, Dcm, Cm e mm

medida =float(input("digitar um medida   "))

cm = medida * 100
mm = medida *1000
dcm = medida *10
Dcam = medida /10
Htm = medida /100
Km = medida /1000

print("o numero digitao é {}, \n o resultado  cm {}, \n  o resultado mm é {},\n  o resultado mm é {},\n  o resultado Dcam é {}  \n  o resultado Htm é {}, \n  o resultado Km é {} ".format(medida,cm,mm,dcm,Dcam, Htm,Km))


