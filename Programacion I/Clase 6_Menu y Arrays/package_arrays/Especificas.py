def mostrar_cantidad_positivos_negativos(lista):
    cantidad_positivos = 0
    cantidad_negativos = 0
    
    for i in range(len(lista)):
        if lista[i] > 0:
            cantidad_positivos += 1
        else:
            cantidad_negativos += 1
    
    return cantidad_positivos, cantidad_negativos


def mostrar_suma_pares(una_lista):
    suma = 0
    
    for i in range(len(una_lista)):
        if una_lista[i] % 2 == 0:
            suma += una_lista[i]
    
    return suma

#resultado = mostar_suma_pares(lista)


def mostrar_mayor_impares(otra_lista):
    
    maximo = otra_lista[0]
    
    for i in range(len(otra_lista)):
        if otra_lista[i] % 2 != 0:
            if otra_lista[i] > maximo:
                maximo = otra_lista[i]
            
    return maximo
            
#resultado = mostrar_mayor_impares(lista)







