def numero_par_impar(numero):
    if numero % 2 == 0:
        return "Es un numero par"
    else:
        return "Es un numero impar"

resultado = numero_par_impar(10)
print(resultado)