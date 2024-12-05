def interpolation_search(array, escolhido):
    esquerda, direita = 0, len(array) - 1
    while esquerda <= direita and escolhido >= array[esquerda] and escolhido <= array[direita]:
        
        if esquerda == direita:
            if array[esquerda] == escolhido:
                return esquerda
            return -1

        pos = esquerda + ((direita - esquerda) // (array[direita] - array[esquerda]) * (escolhido - array[esquerda]))

        if array[pos] == escolhido:
            return pos
        elif array[pos] < escolhido:
            esquerda = pos + 1
        else:
            direita = pos - 1

    return -1

def binary_search(array, escolhido):
    esquerda, direita = 0, len(array) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2 
        if array[meio] == escolhido:  
            return meio
        elif array[meio] < escolhido: 
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1  

array_uniforme = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
escolhido = 70

resultado = interpolation_search(array_uniforme, escolhido)
print(f"Elemento {escolhido} encontrado no índice {resultado} (Uniforme).")

array_nao_uniforme = [5, 10, 25, 50, 90, 200, 500]
escolhido = 90

resultado = interpolation_search(array_nao_uniforme, escolhido)
print(f"Elemento {escolhido} encontrado no índice {resultado} (Não Uniforme).")

import time

def tempo(func, array, escolhido):
    inicio = time.time()
    resultado = func(array, escolhido)
    fim = time.time()
    return resultado, fim - inicio

array_grande_uniforme = list(range(1, 1000001))  
array_grande_nao_uniforme = [x**2 for x in range(1, 1001)]  

result1, tempo1 = tempo(interpolation_search, array_grande_uniforme, 750000)
result2, tempo2 = tempo(interpolation_search, array_grande_nao_uniforme, 250000)

result3, tempo3 = tempo(binary_search, array_grande_uniforme, 750000)
result4, tempo4 = tempo(binary_search, array_grande_nao_uniforme, 250000)

print(f"Interpolation Search (Uniforme): Índice {result1}, Tempo {tempo1:.6f}s")
print(f"Interpolation Search (Não Uniforme): Índice {result2}, Tempo {tempo2:.6f}s")
print(f"Binary Search (Uniforme): Índice {result3}, Tempo {tempo3:.6f}s")
print(f"Binary Search (Não Uniforme): Índice {result4}, Tempo {tempo4:.6f}s")
