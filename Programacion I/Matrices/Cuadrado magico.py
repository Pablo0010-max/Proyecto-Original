def mostrar_cuadrado_magico(otra_matriz):
    numero = len(otra_matriz)
    
    suma = numero * (numero**2 + 1) // 2
    
    for i in range(numero):
        suma_fila = 0
        suma_columna = 0
        
        for j in range(numero):
            suma_fila += int(otra_matriz[i][j])
            suma_columna += int(otra_matriz[j][i])

    suma_diagonales = 0
    for a in range(len(otra_matriz)):
        
        suma_diagonales += int(otra_matriz[a][a])
    
    suma_otra_diagonal = 0
    for b in range(numero):
        
        suma_otra_diagonal += int(otra_matriz[b][numero - 1 - b])


    if suma_columna != suma or suma_fila != suma or suma != suma_diagonales:
        print("Su matriz no es un cuadrado magico.")
    else:
        print("Su matriz es un cuadrado magico.")
    
    return suma_columna, suma_fila, suma_diagonales, suma_otra_diagonal
    


matriz = [[0] * 3 for _ in range(3)]

for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j] = input("Ingrese un valor: ")


resultado = mostrar_cuadrado_magico(matriz)
print(resultado)