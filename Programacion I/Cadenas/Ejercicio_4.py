def suprimir(una_cadena):
    cadena_2 = ""
    for i in range(len(una_cadena)):
        if una_cadena[i] != una_cadena[i - 1]:  
            cadena_2 += una_cadena[i]
            continue
    
    return cadena_2

cadena = "hooola"
resultado = suprimir(cadena)
print(resultado)