def calcular_fibonacci(numero:int) -> int:
    
    if numero == 0:
        return 0
    elif numero == 1:
        return 1
    else:
        suma = calcular_fibonacci(numero -1) + calcular_fibonacci(numero -2)
        return suma

numero = 3
resultado = calcular_fibonacci(numero)
print(f"La suma es: {resultado}")