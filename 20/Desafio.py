import time
import random

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

def shell_sort(array):
    n = len(array)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
        gap //= 2
    return array

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

def selection_sort(array):
    x = len(array)
    passos = [] 
    for i in range(x):
        NuMenor = i
        for n in range(i + 1, x):
            if array[n] < array[NuMenor]:
                NuMenor = n

        array[i], array[NuMenor] = array[NuMenor], array[i]

        passos.append(array.copy())

    return array, passos

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

def counting_sort(array, exp, base):
    x = len(array)
    saida = [0] * x
    conta = [0] * base

    for num in array:
        index = (num // exp) % base
        conta[index] += 1

    for i in range(1, base):
        conta[i] += conta[i - 1]

    for i in range(x - 1, -1, -1):
        index = (array[i] // exp) % base
        saida[conta[index] - 1] = array[i]
        conta[index] -= 1

    return saida

def radix_sort(array, base=10):
    if len(array) == 0:
        return array

    maximo = max(array)
    exp = 1

    while maximo // exp > 0:
        array = counting_sort(array, exp, base)
        exp *= base

    return array
        
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

def main():
    print("Escolha uma opção:")
    print("1. Ordenar a lista")
    print("2. Procurar um elemento")
    opcao = int(input("Digite o número da opção: "))
    
    n = int(input("Quantos números deseja gerar? "))
    lista = [random.randint(0, 100) for _ in range(n)]
    print(f"Lista gerada: {lista}")
    
    if opcao == 1:
        print("Escolha o algoritmo de ordenação:")
        print("1. Shell Sort")
        print("2. Merge Sort")
        print("3. Selection Sort")
        print("4. Bucket Sort")
        print("5. Radix Sort")
        print("6. Quick Sort")
        sort_opcao = int(input("Digite o número do algoritmo: "))
        
        start_time = time.time()
        if sort_opcao == 1:
            sorteio = shell_sort(lista)
        elif sort_opcao == 2:
            sorteio = merge_sort(lista)
        elif sort_opcao == 3:
            sorteio = selection_sort(lista)
        elif sort_opcao == 4:
            sorteio = bucket_sort(lista)
        elif sort_opcao == 5:
            sorteio = radix_sort(lista)
        elif sort_opcao == 6:
            sorteio = quick_sort(lista)
        else:
            print("Opção inválida")
            return
        end_time = time.time()
        print(f"Lista ordenada: {sorteio}")
        print(f"Tempo de execução: {end_time - start_time:.6f} segundos")
    
    elif opcao == 2:
        elemento = int(input("Digite o número a ser procurado: "))
        print("Escolha o algoritmo de busca:")
        print("1. Binary Search")
        print("2. Interpolation Search")
        print("3. Jump Search")
        print("4. Exponential Search")
        print("5. Ternary Search")
        pesquisa = int(input("Digite o número do algoritmo: "))
        
        start_time = time.time()
        if pesquisa == 1:
            index = binary_search(lista, elemento)
        elif pesquisa == 2:
            lista.sort()
            index = interpolation_search(lista, elemento)
        elif pesquisa == 3:
            lista.sort()
            index = jump_search(lista, elemento)
        elif pesquisa == 4:
            lista.sort()
            index = exponential_search(lista, elemento)
        elif pesquisa == 5:
            lista.sort()
            index = ternary_search(lista, elemento)
        else:
            print("Opção inválida")
            return
        end_time = time.time()
        
        if index != -1:
            print(f"Elemento {elemento} encontrado no índice {index}")
        else:
            print(f"Elemento {elemento} não encontrado.")
        print(f"Tempo de execução: {end_time - start_time:.6f} segundos")

if __name__ == "__main__":
    main()
