mi_lista = [-1]*5

bandera_seguir = "si"
while bandera_seguir == "si":
    posicion = int(input(f"Ingrese la posicion entre 1 y {len(mi_lista)}: "))
    while posicion < 1 or posicion > len(mi_lista):
        posicion = int(input(f"Reingrese la posicion entre 1 y {len(mi_lista)}: "))
    
    
    numero = int(input("Ingrese numero: "))
    
    mi_lista[posicion-1] = numero
    
    bandera_seguir = input("Desea seguir? si/no: ")

#MOSTRAR LISTA:
for i in range(len(mi_lista)):
    if mi_lista[i] != -1:
        print(f"{i+1} -> {mi_lista[i]}")