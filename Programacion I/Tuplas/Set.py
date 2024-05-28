#lista = [3,9,3,4,9,9,4,3,5]
#mi_set = set(lista)
#print(mi_set)#No admite duplicados

#mi_set.add(100)#No respeta orden

#for elemento in mi_set:
#    print(elemento)

#mi_set.remove(40)Tira error
#mi_set.discard(30)#No borra nada

#elemento = mi_set.pop()#Elimina el primero
#print(elemento)

#mi_set.clear()


set_a = {3,4,5}
set_b = {6,2,3}

union = set_a.union(set_b)
print(union)

interseccion = set_a.intersection(set_b)
print(interseccion)

diferencia = set_a.difference(set_b)
print(diferencia)
