def closetnumber(arr):

    arreglo_ordenado = sorted(arr)
    diferenciaMin = arreglo_ordenado[1] - arreglo_ordenado[0]
    resultado = []

    for i in range(len(arreglo_ordenado)-1):
        diferenciaAtual = arreglo_ordenado[i+1] - arreglo_ordenado[i]

        if (diferenciaAtual< diferenciaMin):
            resultado = []

        if (diferenciaAtual<=diferenciaMin):
            resultado.append(arreglo_ordenado[i])
            resultado.append(arreglo_ordenado[i+1])
            diferenciaMin = diferenciaAtual
    
    for i in range(0, len(resultado)-1,2):   # vamos imprimir por duplas por ese el 2.
        print(f'{resultado[i]} {resultado[i+1]}')


closetnumber([40,8,2,10,5,15,20,21,30,31])    
