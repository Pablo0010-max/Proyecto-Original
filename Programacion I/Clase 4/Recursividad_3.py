def sumar_digitos(numero:int) -> int:
    
    if numero == 0:
        return 0
    else:
        numero_digito = numero % 10
        numero = numero // 10
        suma = numero_digito + sumar_digitos(numero)
        return suma

numero = 412
resultado = sumar_digitos(numero)
print(f"el digito es: {resultado}")
