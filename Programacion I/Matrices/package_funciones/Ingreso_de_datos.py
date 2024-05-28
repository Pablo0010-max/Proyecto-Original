from Funciones import *

legajos = [[110, 133, 127, 117, 102], 
            [203, 207, 211, 244, 230],
            [303, 315, 321, 327, 340]]
matriz = [[0] * 3 for _ in range(5)]
bandera_ingreso = True
bandera_seguir = False

while bandera_ingreso == True:
    opciones = int(input("1.Ingresar legajo\n2.Ingresar recaudacion del viaje\nElija una opcion:"))
    
    match opciones:
        case 1:
            numero = int(input("Ingrese su N° de legajo:"))
            for i in range(len(legajos)):
                if numero == legajos[i]:
                    bandera_seguir == True
            else:
                
                print("Ese legajo no se encuentra")
                break
    
        case 2:
            if bandera_seguir == True:
                coche = int(input("Ingrese su coche:"))
                linea = int(input("Ingrese su linea:"))
                recaudacion = int(input("Ingrese su recaudacion"))
                resultado = mostrar_matriz(matriz, coche, linea, recaudacion)
            
            
            
    