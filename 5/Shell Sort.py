import time


def shell_sort(array, gap_sequence):
    n = len(array)
    for gap in gap_sequence:
        for i in range(gap, n):
            temp = array[i]
            j = i
            while j >= gap and array[j - gap] > temp:
                array[j] = array[j - gap]
                j -= gap
            array[j] = temp
    return array

def medir_tempo(func, array, gap_sequence):
    inicio = time.time()
    resultado = func(array.copy(), gap_sequence)
    fim = time.time()
    return resultado, fim - inicio

array = [54, 26, 93, 17, 77, 31, 44, 55, 20]

n = len(array)
gaps_shell = [n // 2**k for k in range(int(n**0.5)+1) if n // 2**k > 0]
gaps_knuth = [int((3**k - 1) / 2) for k in range(1, 10) if (3**k - 1) / 2 < n]
gaps_hibbard = [2**k - 1 for k in range(1, 10) if 2**k - 1 < n]

for nome, gaps in [("Shell", gaps_shell), ("Knuth", gaps_knuth), ("Hibbard", gaps_hibbard)]:
    _, tempo = medir_tempo(shell_sort, array, gaps)
    print(f"Ordenação usando {nome}: Tempo {tempo:.6f}s")
