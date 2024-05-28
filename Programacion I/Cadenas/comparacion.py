#Tabla ASCII
cadena = "hola"

print(cadena < "azul")
print(cadena < "Perro")#h(104) P(80)


nombres = ["Belen", "Mauro", "Mauricio", "Zoe", "Ana"]

for i in range(0, len(nombres)-1):
    for j in range(i + 1, len(nombres)):
        if nombres[i] > nombres[j]:
            auxiliar = nombres[i]
            nombres[i] = nombres[j]
            nombres[j] = auxiliar

print(nombres)

cadena = "HOLA C3MO ESTAN"
cadena_2 = ""
for i in range(len(cadena)):
    if cadena[i] == "O":
        cadena_2 += "*"
        continue
    
    cadena_2 += cadena[i]

for i in range(len(cadena)):
    caracter_minuscula = cadena[i]
    if cadena[i] >= "A" and cadena[i] <= "Z":
        orden = ord(cadena[i]) + 32
        caracter_minuscula = chr(orden)
        
        
    cadena_2 += caracter_minuscula

print(cadena_2)


def buscar_caracter_valido(busqueda, caracteres):
    encontro = False
    for i in range(len(caracteres)):
        if caracteres[i] == busqueda:
            encontro = True
            break
    
    return encontro


caracteres_validos = "IVXCLDM"

for i in range(len(cadena)):
    caracter = cadena[i]
    if buscar_caracter_valido(caracter, caracteres_validos):
        orden = ord(caracter) + 32
        caracter = chr(orden)
    
    cadena_2 += caracter