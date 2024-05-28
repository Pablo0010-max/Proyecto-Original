array = [1,4,3,5,2]

for i in range(0, len(array)-1):
    for j in range(i + 1, len(array)):
        if array[i] > array[j]:
            auxiliar = array[i]
            array[i] = array[j]
            array[j] = auxiliar