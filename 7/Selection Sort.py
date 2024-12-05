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

ListaPequena = [78, 20, 12, 54]
ListaMedia = [64, 25, 12, 22, 11, 3]
ListaGrande = [3, 6, 24, 50, 45, 54, 40, 30, 8]

result, interacoes = selection_sort(ListaPequena)

print("Organização da lista:")
for i, passo in enumerate(interacoes, start=1):
    print(f"Iteração {i}: {passo}")

print(f"Lista Pequena Ordenada: {result}\n")


result, interacoes = selection_sort(ListaMedia)

print("Organização da lista:")
for i, passo in enumerate(interacoes, start=1):
    print(f"Iteração {i}: {passo}")

print(f"Lista Media Ordenada: {result}\n")


result, interacoes = selection_sort(ListaGrande)

print("Organização da lista:")
for i, passo in enumerate(interacoes, start=1):
    print(f"Iteração {i}: {passo}")

print(f"Lista Grande Ordenada: {result}")
