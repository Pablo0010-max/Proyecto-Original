from class_boligrafo import Boligrafo

boligrafo_1 = Boligrafo("Fino", "Azul")
boligrafo_2 = Boligrafo("Grueso", "Rojo")

print(f"Boligrafo 1: {boligrafo_1.escribir("hola")}")
print(f"Boligrafo 2: {boligrafo_2.escribir("hola")}")

print(f"Boligrafo 1: {boligrafo_1.recargar(40)}")
print(f"Boligrafo 2: {boligrafo_2.recargar(20)}")



