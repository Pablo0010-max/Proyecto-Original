def mostrar_lista(lista_numeros):
    
    print(f"Numeros ingresados: {lista_numeros}")

#resultado = mostar_lista(lista)


def mostrar_pares(lista_pares):
    lista_p = []
    
    for i in range(len(lista_pares)):
        if lista_pares[i] % 2 == 0:
            lista_p += [lista_pares[i]]
    
    return print(f"Los numeros pares son: {lista_p}")

#resultado = mostar_pares(lista)


def mostrar_posiciones_impares(lista_posiciones):
    lista_i = []
    
    for i in range(len(lista_posiciones)):
        if i % 2 != 0:
            lista_i += [lista_posiciones[i]-1]
    
    return print(f"Los numeros en posiciones impares son: {lista_i}")