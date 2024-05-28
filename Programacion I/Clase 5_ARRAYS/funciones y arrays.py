def mostrar_enteros(una_lista: list):
    suma_lista = 0
    for i in range(len(una_lista)):
        suma_lista += (una_lista[i])
    
    resultado = suma_lista / len(una_lista)
    
    return resultado
    
mi_lista = [-4,8,6,9,10]
#promedio = mostrar_enteros(mi_lista)
#print(f"El promedio es: {promedio}")



def mostar_promedio_positivos(otra_lista: list):
    numeros_positivos = 0
    cantidad_positivos = 0
    
    for i in (otra_lista):
        if i > 0:
            numeros_positivos += i
            cantidad_positivos += 1
            
    resultado = numeros_positivos / cantidad_positivos
            
    return resultado
    
        





#positivos = mostar_promedio_positivos(mi_lista)
#print(f"El promedio de los numeros positivos es: {positivos}")


def mostrar_producto(lista_1: list):
    cuenta = 1
    
    if type (lista_1) == list:
        
        for i in range(len(lista_1)):
            cuenta *= (lista_1[i])
        
        return cuenta

#producto = mostrar_producto(mi_lista)
#print(f"El producto es: {producto}")

def mostar_valor_max(lista_2: list):
    maximo = lista_2[0]
    for i in (lista_2):
        if i > maximo:
            maximo = i
    
    return maximo

#valor_maximo = mostar_valor_max(mi_lista)
#print(f"El numero maximo es: {valor_maximo}")


def mostar_posicion_valor_max(lista_3: list):
    maximo = lista_3[0]
    
    for i in (lista_3):
        
        if i > maximo:
            maximo = i
    for i in range(len(lista_3)):
        if lista_3[i] == maximo:
            posicion = i
            
    return posicion
    

#posicion_maximo = mostar_valor_max(mi_lista)
#print(f"La posicion del numero maximo es: {posicion_maximo}")


nombres_lista = ["Pablo", "Tomas", "Pepe"]

def remplazar_nombre(lista_nom: list, nombre_remplazado: str, remplazante: str ):
    cantidad_remplazos = 0
    for i in range(len(lista_nom)):
        if lista_nom[i] == nombre_remplazado:
            lista_nom[i] = remplazante
            cantidad_remplazos += 1
    
    return (f"{lista_nom} se realizo {cantidad_remplazos} remplazo")





nombres = remplazar_nombre(nombres_lista, "Pepe", "Santiago")
print(f"-> {nombres}")