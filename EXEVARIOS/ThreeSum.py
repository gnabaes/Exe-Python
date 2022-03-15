def three_number_sum(arreglo, sumaobj):
    arreglo.sort()    # para ordenar el array o vector
    tripletes = []

    for numero_actual in range(len(arreglo)-2):
        puntero_izq = numero_actual +1
        puntero_der = len(arreglo) - 1

        while puntero_izq < puntero_der:
            sum_atual = arreglo[numero_actual]+arreglo[puntero_izq]+arreglo[puntero_der]
            if sum_atual == sumaobj:
                tripletes.append([arreglo[numero_actual],arreglo[puntero_izq],arreglo[puntero_der]])
                puntero_izq += 1
                puntero_der -= 1
            elif sum_atual < sumaobj:
                puntero_izq += 1
            elif sum_atual > sumaobj:
                puntero_der -= 1
    return tripletes


print(three_number_sum([-7,-1,8,-10,6,4,-8,1,7],0))