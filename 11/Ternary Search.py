import time
import random

def ternary_search(array, esquerdo, direito, escolhido):
    if direito >= esquerdo:
        mid1 = esquerdo + (direito - esquerdo) // 3
        mid2 = direito - (direito - esquerdo) // 3
        if array[mid1] == escolhido:
            return mid1
        if array[mid2] == escolhido:
            return mid2
        if escolhido < array[mid1]:
            return ternary_search(array, esquerdo, mid1 - 1, escolhido)
        elif escolhido > array[mid2]:
            return ternary_search(array, mid2 + 1, direito, escolhido)
        else:
            return ternary_search(array, mid1 + 1, mid2 - 1, escolhido)
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

n = int(input("Quantos números deseja gerar? "))
array = sorted([random.randint(0, 100) for _ in range(n)])

print(f"Lista gerada: {array}")

elemento = int(input("Digite o número a ser procurado: "))

start_time = time.time()
index_binary = binary_search(array, elemento)
end_time = time.time()
print(f"Binary Search: Elemento {elemento} encontrado no índice {index_binary}" if index_binary != -1 else "Elemento não encontrado")
print(f"Tempo de execução do Binary Search: {end_time - start_time:.6f} segundos")

start_time = time.time()
index_ternary = ternary_search(array, 0, len(array) - 1, elemento)
end_time = time.time()
print(f"Ternary Search: Elemento {elemento} encontrado no índice {index_ternary}" if index_ternary != -1 else "Elemento não encontrado")
print(f"Tempo de execução do Ternary Search: {end_time - start_time:.6f} segundos")
