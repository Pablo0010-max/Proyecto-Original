
from class_personaje import Personaje

personaje_1 = Personaje("IronMan", 500, "Disparo ultrasonico", True, True)
personaje_2 = Personaje("Thor", 710, "Trueno", False, False)
personaje_3 = Personaje("Blackwidow", 800, "Pelea cuaerpo a cuerpo", False, False)
personaje_4 = Personaje("SpiderMan", 500, "Muerte instantanea", False, True)

lista_heroes:list[Personaje] = []

lista_heroes.append(personaje_1)
lista_heroes.append(personaje_2)
lista_heroes.append(personaje_3)
lista_heroes.append(personaje_4)

for heroe in lista_heroes:
    print(heroe.describirse())

for heroe in lista_heroes:
    heroe.volar(1000,200)

descripcion = personaje_1.describirse()
print(descripcion)
print(personaje_2.describirse())

personaje_1.volar(1000, 200)
personaje_2.volar(200, 150)

personaje_1.atacar(personaje_2)
print(personaje_1.poder_pelea)
print(personaje_2.poder_pelea)



