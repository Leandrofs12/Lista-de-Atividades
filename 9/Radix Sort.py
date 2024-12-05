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

num2dig = [170, 45, 75, 90, 802, 24, 2, 66, 66]
num5dig = [12345, 54321, 67890, 98765, 11111]
num10dig = [9876543210, 1234567890, 1122334455, 9988776655]
ordem = radix_sort(num2dig)
print("Lista ordenada: \n", ordem)
ordem = radix_sort(num5dig)
print("Lista ordenada: \n", ordem)
ordem = radix_sort(num10dig)
print("Lista ordenada:", ordem)
