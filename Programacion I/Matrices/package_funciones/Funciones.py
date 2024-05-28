from Ingreso_de_datos import matriz

def mostrar_matriz(una_matriz, un_coche, una_linea, una_recaudacion):
    
    for i in range(len(una_matriz)):
        if i == un_coche:
            for j in range(len(matriz[i])):
                if j == una_linea:
                    matriz[un_coche - 1][una_linea - 1] = una_recaudacion
        
    return una_recaudacion





