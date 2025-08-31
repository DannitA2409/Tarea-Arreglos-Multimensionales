matriz = [
    [4, 7, 1],
    [9, 3, 5],
    [2, 8, 6]
]

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return True, (i, j)  # se encontró el valor
    return False, (-1, -1)  # no se encontró el valor

valor_a_buscar = 5

encontrado, posicion = buscar_valor(matriz, valor_a_buscar)

if encontrado:
    print(f"El valor '{valor_a_buscar}' se encontró en la fila: {posicion[0]}, columna: {posicion[1]}")
else:
    print(f"El valor {valor_a_buscar} no se encuentra en la matriz.")