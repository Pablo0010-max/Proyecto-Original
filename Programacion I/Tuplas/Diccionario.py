mi_diccionario = {
    "nombre": "Juan",
    "edad": 25,
    "ciudad": "Mendoza"
}
mi_diccionario["nombre"] = "Luis"

#print(mi_diccionario["nombre"])
#print(mi_diccionario["ciudad"])

mi_diccionario["profesion"] = "Programador"


print(mi_diccionario)

print(mi_diccionario.keys())
print(mi_diccionario.values())
print(mi_diccionario.items())

#for clave in mi_diccionario:
#    print(mi_diccionario[clave])

for clave, valor in mi_diccionario.items():
    print(f"{clave} -> {valor}")