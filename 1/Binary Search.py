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


array = [10, 20, 30, 40, 50, 60, 70,80, 90, 100]
escolhido = 10

index = binary_search(array, escolhido)
if index != -1:
    print(f"Elemento {escolhido} encontrado no índice {index}.")
else:
    print(f"Elemento {escolhido} não encontrado.")
