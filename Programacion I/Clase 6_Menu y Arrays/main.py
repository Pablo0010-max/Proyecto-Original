from package_arrays.Especificas import *
from package_arrays.Array_generales import *
from os import system

system("cls")
lista_numeros = []*10
bandera_seguir = True
bandera_ingreso = False

while bandera_seguir == True:
    opcion = int(input("1. Ingrese 10 numeros entre -1000 y 1000\n2.Cantidad de numeros positivos y negativos\n3.Suma de numeros pares\n4.Mayor de numeros impares\n5.Lista de numeros ingresados\n6.Lista de numeros pares\n7.Numeros en posiciones impares\n8.Salir\n9.Elija una opcion: "))
    
    
    match opcion:
        case 1:
            lista_numeros = []
            for i in range(10):
                numero = int(input("Ingrese el número: "))
                lista_numeros += [numero]
            bandera_ingreso = True
        case 2:
            if bandera_ingreso == True:
                positivos, negativos = mostrar_cantidad_positivos_negativos(lista_numeros)
                print(f"La cantidad de postitivos es de: {positivos}\nLa cantidad de negativos es de: {negativos}")
        case 3:
            if bandera_ingreso == True:
                suma = mostrar_suma_pares(lista_numeros)
                print(f"La suma de los numeros pares es de: {suma}")
        case 4:
            if bandera_ingreso == True:
                mayor_impares = mostrar_mayor_impares(lista_numeros)
                print(f"El mayor de los numeros impares es: {mayor_impares}")
        case 5:
            if bandera_ingreso == True:
                lista = mostrar_lista(lista_numeros)
        case 6:
            if bandera_ingreso == True:
                pares = mostrar_pares(lista_numeros)
        case 7:
            if bandera_ingreso == True:
                posicion_impares = mostrar_posiciones_impares(lista_numeros)
        case 8:
            bandera_ingreso == False
            break
    
    system("pause")
    system("cls")