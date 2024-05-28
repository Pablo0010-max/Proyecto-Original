def recibir_precio(precio:int, cantidad:int,) -> int:
    if cantidad == 0:
        return 0 
    elif cantidad > 10: 
        porcentaje = (cantidad/precio)*100
        return porcentaje



precio: 10
cantidad: 15
resultado = recibir_precio(precio, cantidad)
print = (resultado)