def mostrar_vocales(cadena_1, cantidad_a, cantidad_e, cantidad_i, cantidad_o, cantidad_u, una_matriz):
    
    for i in range(len(cadena_1)):
        if cadena[i] == "a":
            cantidad_a += 1
        elif cadena_1[i] == "e":
            cantidad_e += 1
        elif cadena[i] == "i":
            cantidad_i += 1
        elif cadena_1[i] == "o":
            cantidad_o += 1
        elif cadena_1[i] == "u":
            cantidad_u += 1
    
    cantidades = [cantidad_a, cantidad_e, cantidad_i, cantidad_o, cantidad_u]
    
    for i in range(len(una_matriz)):
        una_matriz[i][0] = vocales[i]
        una_matriz[i][1] = cantidades[i] 
        
    return una_matriz


contador_a = 0
contador_e = 0
contador_i = 0
contador_o = 0
contador_u = 0
cadena = "murcielaguito"
vocales = ["a", "e", "i", "o", "u"]

matriz = [[0] * 2 for _ in range(5)]

resultado = mostrar_vocales(cadena, contador_a, contador_e, contador_i, contador_o, contador_u, matriz)
print(resultado)
