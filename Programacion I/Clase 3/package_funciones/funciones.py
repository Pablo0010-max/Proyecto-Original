
def get_int(mensaje:str = "Ingrese numero", mensaje_error:str = "Reingrese numero", minimo:int = 10, maximo:int = 50, reintentos:int = 3) -> int|None:
    
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


def get_float(mensaje:str = "Ingrese numero", mensaje_error:str = "Reingrese numero", minimo:float = 10.0, maximo:float = 50.0, reintentos:int = 3) -> float|None:
    
    intentos = 0
    numero_ingresado = input(mensaje)
    numero_ingresado = float(numero_ingresado)
    while numero_ingresado < minimo or numero_ingresado > maximo:
        intentos += 1
        numero_ingresado = input(f"ERROR {mensaje_error}")
        numero_ingresado = float(numero_ingresado)
        if intentos == reintentos:
            print("Exediò")
            return None

    print(numero_ingresado)
    
def get_string(longitud: int) -> str|None:
    longitud = input("Ingrese longitud")
    longitud = len(longitud)
    return longitud