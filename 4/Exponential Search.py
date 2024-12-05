import math
import time


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

def exponential_search(array, escolhido):
    n = len(array)
    if n == 0:
        return -1

    if array[0] == escolhido:
        return 0

    i = 1
    while i < n and array[i] <= escolhido:
        i *= 2

    return binary_search(array, escolhido, i // 2, min(i, n - 1))

array = [2, 3, 4, 10, 40, 80, 120, 160, 200, 240]
escolhido = 40

resultado = exponential_search(array, escolhido)
if resultado != -1:
    print(f"Elemento {escolhido} encontrado no índice {resultado}.")
else:
    print(f"Elemento {escolhido} não encontrado.")


import time

def medir_tempo(func, array, escolhido):
    inicio = time.time()
    resultado = func(array, escolhido)
    fim = time.time()
    return resultado, fim - inicio

listas = {
    "Pequena": list(range(1, 101)),       
    "Média": list(range(1, 10001)),      
    "Grande": list(range(1, 1000001)),   
}

escolhido = 5000

for nome, lista in listas.items():
    print(f"\nLista {nome} ({len(lista)} elementos):")

    res_exp, tempo_exp = medir_tempo(exponential_search, lista, escolhido)
    print(f"Exponential Search: Índice {res_exp}, Tempo {tempo_exp:.6f}s")

    res_binary, tempo_binary = medir_tempo(binary_search, lista, escolhido)
    print(f"Binary Search: Índice {res_binary}, Tempo {tempo_binary:.6f}s")

