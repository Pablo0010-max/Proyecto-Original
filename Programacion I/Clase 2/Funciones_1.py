def ingresar_numero(numero:int) -> int:
    
    return numero

numero = 5
resultado = ingresar_numero(numero)
print(resultado)


def ingresar_flotante(numero_float:float) -> float:
    
    return numero_float

numero_float = 10
resultado_1 = ingresar_numero(numero_float)
print(resultado_1)


def ingresar_cadena(cadena:str) -> str:
    
    return cadena

cadena = "HOLA"
resultado_2 = ingresar_numero(cadena)
print(resultado_2)


def calcular_area(radio:int) -> int:
    radio = radio * radio
    area = numero_pi * radio
    return area

radio = 4
numero_pi = 3.14
resultado = calcular_area(radio)
print(resultado)


def encontrar_maximo(numero_1:int, numero_2:int, numero_3:int) ->int:
    if numero_1 > numero_2 and numero_1 > numero_3:
        return numero_1
    elif numero_2 > numero_1 and numero_2 > numero_3:
        return numero_2
    else:
        return numero_3
        

numero_1 = 3
numero_2 = 4
numero_3 = 5
numero = encontrar_maximo(numero_1, numero_2, numero_3)
print(numero)

def calcular_potencia(base:int, exponente:int) ->int:
    numero = base * exponente
    return numero


base = 2
exponente = 3
resultado = calcular_potencia(base, exponente)
print(resultado)