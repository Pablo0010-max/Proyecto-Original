def swap(a: int, b: int): # Intercambia los valores de 'a' y 'b'
    return b, a

def particionar(array, low, high):
    pivote = array[high] # El pivote sera el ultimo elemento de la lista, en este caso 2
    i = low - 1

    for j in range(low, high):
        if array[j] <= pivote: # 1 <= 2 # 4 <= 2 # 3 <= 2 # 5 <= 2
            array_j = array[j]
            i += 1
            array_i = array[i]
            array[i], array[j] = swap(array[i], array[j]) # 1, 1
    array[i + 1], array[high] = swap(array[i + 1], array[high]) # 2, 4

    return i + 1 # 0 + 1 = 1

def quick_sort(array, low, high):
    while True:
        if low < high: # 0 < 4
            pi = particionar(array, low, high)
            high = pi - 1
        else:
            return array

# vector = [1, 4, 3, 5, 2, 8, 6, 7, 9]
vector = [5,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,1,9,7,3,1,9,7,3,1,9,7,
          3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,
          9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,
          3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,
          9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,
          1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,
          3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,
          9,7,3,1,9,7,3,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,
          3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,
          7,3,1,9,7,3,1,9,7,3,1,9,7,3,1,9,7,3,7,3,1,9,7,3,1,9,7]

quick_sort(vector, 0 , len(vector) - 1)

import time

start = time.time()
quick_sort(vector, 0 , len(vector) - 1)
end = time.time()

print(end)
print(start)
print(f"Tiempo: {(end - start) * 1000}")

print(f"Vector: {vector}")