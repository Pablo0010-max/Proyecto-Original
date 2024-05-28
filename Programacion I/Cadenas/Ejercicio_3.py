def mostrar_palidromo(una_cadena, desde, hasta, reverse = False):
    incremento = -1
    bandera = False
    if reverse == True:
        aux = desde
        desde = hasta -1
        hasta = aux -1
        incremento = -1
        for i in range(desde, hasta, incremento):
            for j in range(len(una_cadena)):
                if una_cadena[i] == una_cadena[j]:
                    bandera = True
                else:
                    bandera = False
    
    return bandera

cadena = "neuquen"
resultado = mostrar_palidromo(cadena, 0, len(cadena), True)
print(resultado)