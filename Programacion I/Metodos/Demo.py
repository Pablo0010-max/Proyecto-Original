cadena = "   Hola     "#lstrip()/ rstrip()
cadena = cadena.strip()

print(cadena)


cadena_1 = "HOLA MUNDO"
cadena_1 = cadena_1.lower()#capitalize -> Hola mundo
print(cadena_1)

#title -> Hola Mundo

cadena_2 = "lalala hola como estan"
cadena_2 = cadena_2.replace("la", "<3")
print(cadena_2)


cadena_3 = "Python,Java,C,C#"
listas_lenguajes = cadena_3.split(",")
print(listas_lenguajes)

lista = ["Java", "C", "C#", "Python"]
delimitador = "*"
cadena_4 = delimitador.join(lista)
print(cadena_4)

numero = "4"
print(numero.zfill(10))

cadea_5 = "123aaa"
print(cadea_5.isalpha())

