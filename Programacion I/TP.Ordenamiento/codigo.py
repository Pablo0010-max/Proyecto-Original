import time

def sort_list_descending(array: list[int]) -> None:
    n = len(array)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if array[j] > array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]

array = [6, 5, 2, 7, 4, 1, 0, 3]

start = time.time()
sort_list_descending(array)
end = time.time()

print(f"Tiempo: {(end - start) * 1000} ms")
print(array)
