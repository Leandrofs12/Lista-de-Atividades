import time
import random
import sys

sys.setrecursionlimit(10**5)

def quick_sort(array, escolha_pivo="ultimo"):
    if len(array) <= 1:
        return array

    if escolha_pivo == "primeiro":
        pivo = array[0]
    elif escolha_pivo == "ultimo":
        pivo = array[-1]
    elif escolha_pivo == "meio":
        pivo = array[len(array) // 2]
    else:
        raise ValueError("Estratégia de pivô inválida")

    menor = [x for x in array if x < pivo]
    igual = [x for x in array if x == pivo]
    maior = [x for x in array if x > pivo]

    return quick_sort(menor, escolha_pivo) + igual + quick_sort(maior, escolha_pivo)

def teste():
    sizes = [10, 100, 1000, 10000]
    criterios = ["primeiro", "ultimo", "meio"]

    for size in sizes:
        print(f"\nLista de tamanho {size}:")

        lista = [''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10)) for _ in range(size)]
        quase_ordenada = sorted(lista)
        quase_ordenada[size // 2] = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))

        for criterio in criterios:
            start = time.time()
            quick_sort(lista, criterio)
            random_elapsed = time.time() - start

            start = time.time()
            quick_sort(quase_ordenada, criterio)
            temp = time.time() - start
            print(f"Estratégia: {criterio} | Desordenada: {random_elapsed:.6f}s | Quase ordenada: {temp:.6f}s")

teste()
