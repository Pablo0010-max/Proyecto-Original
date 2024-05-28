def sumar_naturales(numero:int) -> int:
    
    if numero == 0:
        return 0
    else:
        suma = numero + sumar_naturales(numero -1)
        return suma

numero = 5
suma = sumar_naturales(numero)

print(f"La suma de los numeros naturales es: {suma}")