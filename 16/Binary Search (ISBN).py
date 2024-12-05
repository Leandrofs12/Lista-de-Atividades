def binary_search(array, escolhido):
    esquerda, direita = 0, len(array) - 1
    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if array[meio][0] == escolhido:  
            return meio
        elif array[meio][0] < escolhido:
            esquerda = meio + 1
        else:
            direita = meio - 1
    return -1  

livros = [
    (9780131101202, "Biografia CR7",),
    (9780201611340, "Estruturas de Dados",),
    (9783413091111, "Entendendo Algoritmos",),
    (9783413093413, "Turma da Mônica",)]

escolhido = 9783413091111

index = binary_search(livros, escolhido)
if index != -1:
    livro = livros[index]
    print(f"Livro encontrado: ISBN: {livro[0]}, Título: {livro[1]}")
else:
    print(f"Livro com ISBN {escolhido} não encontrado.")
