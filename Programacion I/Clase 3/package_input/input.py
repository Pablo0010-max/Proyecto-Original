def get_int(mensaje:str , mensaje_error:str , minimo:int , maximo:int , reintentos:int ) -> int|None:
    
    intentos = 0
    numero = input(mensaje)
    numero = int(numero)
    while numero < minimo or numero > maximo:
        intentos += 1
        numero = input(f"ERROR {mensaje_error}")
        numero = int(numero)
        if intentos == reintentos:
            print("Exediò")
            return None

    print(numero)


def get_float(mensaje_1:str , mensaje_error_1:str , minimo_1:float , maximo_1:float , reintentos_1:int ) -> float|None:
    
    intentos = 0
    numero_ingresado = input(mensaje_1)
    numero_ingresado = float(numero_ingresado)
    while numero_ingresado < minimo_1 or numero_ingresado > maximo_1:
        intentos += 1
        numero_ingresado = input(f"ERROR {mensaje_error_1}")
        numero_ingresado = float(numero_ingresado)
        if intentos == reintentos_1:
            print("Exediò")
            return None

    print(numero_ingresado)
    
def get_string(longitud: int) -> str|None:
    cadena_ingresada = input("Ingrese una cadena de texto:")
    cadena_ingresada = len(cadena_ingresada)
    if cadena_ingresada == longitud:
        return cadena_ingresada
    else:
        return None