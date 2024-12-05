def bucket_sort(array):
    x = len(array)
    if x == 0:
        return array

    buckets = [[] for _ in range(x)]

    for num in array:
        index = int(num * x)  
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    combinar = []
    for bucket in buckets:
        combinar.extend(bucket)

    return combinar

lista = [0.40, 0.21, 0.30, 0.45, 0.37, 0.48, 0.55]
resultado = bucket_sort(lista)
print("Lista ordenada:", resultado)
