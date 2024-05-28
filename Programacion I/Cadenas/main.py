cadena = "Hola, como estan?"

print(cadena[0])
print(cadena[1])


print(type(cadena))


def slicing(cadena, desde, hasta):
    for i in range(desde, hasta):
        print(cadena[i], end ="")
    

def slicing(cadena, desde, hasta, reverse = False):
    incremento = -1
    if reverse == True:
        aux = desde
        desde = hasta -1
        hasta = aux -1
        incremento = -1
    for i in range(desde, hasta, incremento):
        print(cadena[i], end ="")

slicing(cadena, 0, 4)
print()
#Slicing
print(cadena[0, 4])
print(cadena[5, 10])
slicing(cadena, 5, 10)

slicing(cadena, 0, len(cadena), True)

#repeticion

cadena = "Pedro"
print(cadena * 3)