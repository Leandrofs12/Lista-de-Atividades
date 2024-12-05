def bucket_sort(array):
    if len(array) == 0:
        return array

    maximo = max(array)
    size = len(array)

    buckets = [[] for _ in range(size)]

    for num in array:
        index = num * size // (maximo + 1)
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    combinar = []
    for bucket in buckets:
        combinar.extend(bucket)

    return combinar

lista = [62, 12, 62, 98, 10, 24, 11, 67]
resultado = bucket_sort(lista)
print("Lista ordenada:", resultado)