def merge_sort(array):
    if len(array) <= 1:
        return array

    meio = len(array) // 2
    esquerda = merge_sort(array[:meio])
    direita = merge_sort(array[meio:])

    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = x = 0

    while i < len(esquerda) and x < len(direita):
        if esquerda[i] <= direita[x]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[x])
            x += 1

    resultado.extend(esquerda[i:])
    resultado.extend(direita[x:])
    return resultado

numeros = [38, 27, 43, 3, 9, 82, 10, 3]

resultado = merge_sort(numeros)
print(f"Lista ordenada: {resultado}")

