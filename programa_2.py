matriz = [
    [9, 3, 5],
    [7, 2, 8],
    [4, 6, 1]
]

def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]
    return fila

# Fila a ordenar (teniendo en cuenta el índice 0)
fila_a_ordenar = 2

print("Matriz original:")
for fila in matriz:
    print(fila)

# Ordenamos la fila
matriz[fila_a_ordenar] = bubble_sort(matriz[fila_a_ordenar])

print(f"\nFila a ordenar: {fila_a_ordenar + 1}")

print(f"\nMatriz con la fila {fila_a_ordenar + 1} ordenada:")
for fila in matriz:
    print(fila)