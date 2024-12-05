def bucket_sort(array):
    if len(array) == 0:
        return array

    maximo = max(array)
    minimo = min(array)
    size = len(array)

    buckets = [[] for _ in range(size)]

    for num in array:
        index = (num - minimo) * (size - 1) // (maximo - minimo)  
        buckets[index].append(num)

    for bucket in buckets:
        bucket.sort()

    combinar = []
    for bucket in buckets:
        combinar.extend(bucket)

    return combinar

def interpolation_search(array, escolhido):
    esquerda, direita = 0, len(array) - 1
    while esquerda <= direita and escolhido >= array[esquerda] and escolhido <= array[direita]:
        if array[esquerda] == array[direita]:
            if array[esquerda] == escolhido:
                return esquerda
            return -1

        pos = esquerda + ((direita - esquerda) * (escolhido - array[esquerda])) // (array[direita] - array[esquerda])

        if pos < esquerda or pos > direita:
            return -1  

        if array[pos] == escolhido:
            return pos
        elif array[pos] < escolhido:
            esquerda = pos + 1
        else:
            direita = pos - 1

    return -1

notas = [62, 12, 47, 98, 10, 24, 11, 67, 53, 88, 75, 37, 56, 42, 5, 89, 70, 34, 26, 82]

notas_ordenadas = bucket_sort(notas)
print("Notas:", notas_ordenadas)

nota_especifica = 75
index = interpolation_search(notas_ordenadas, nota_especifica)

if index != -1:
    print(f"A nota {nota_especifica} foi encontrada no índice {index}.")
else:
    print(f"A nota {nota_especifica} não foi encontrada.")
