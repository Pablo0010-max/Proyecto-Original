def encontrar_caracter(una_cadena, un_caracter):
    
    for i in range(len(una_cadena)):
        if una_cadena[i] == un_caracter:
            posicion = i + 1
            return posicion
    
    return -1
    

cadena = "auto"
caracter = "p"
resultado = encontrar_caracter(cadena, caracter)
print(resultado)