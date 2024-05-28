def calcular_potencia(base:int , exponente:int) -> int:
    
    if exponente == 0:
        numero = 1
    else:
        numero = base * calcular_potencia(base, exponente -1)
    
    return numero
    

base = 2
exponente = 3
resultado = calcular_potencia(base, exponente)
print(resultado)