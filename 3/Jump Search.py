import math
import time

def jump_search(array, escolhido):
    n = len(array)
    salto = int(math.sqrt(n))  
    anterior = 0

    while anterior < n and array[min(salto, n) - 1] < escolhido:
        anterior = salto
        salto += int(math.sqrt(n))
        if anterior >= n:
            return -1

    for i in range(anterior, min(salto, n)):
        if array[i] == escolhido:
            return i

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

array = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
escolhido = 13

resultado = jump_search(array, escolhido)
if resultado != -1:
    print(f"Elemento {escolhido} encontrado no índice {resultado}.")
else:
    print(f"Elemento {escolhido} não encontrado.")


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

    # Teste Jump Search
    res_jump, tempo_jump = medir_tempo(jump_search, lista, escolhido)
    print(f"Jump Search: Índice {res_jump}, Tempo {tempo_jump:.6f}s")

    # Teste Binary Search
    res_binary, tempo_binary = medir_tempo(binary_search, lista, escolhido)
    print(f"Binary Search: Índice {res_binary}, Tempo {tempo_binary:.6f}s")

