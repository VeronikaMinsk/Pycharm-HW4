# Напишите функцию для транспонирования матрицы

def transpose_matrix(matrix):

    rows = len(matrix)
    cols = len(matrix[0]) if rows > 0 else 0


    transposed = [[0] * rows for _ in range(cols)]


    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]

    return transposed

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]


transposed_matrix = transpose_matrix(matrix)
print('\nИсходная матрица:')
for row in matrix:
    print(row)


print('\nТранспонированная матрица:')
for row in transposed_matrix:
    print(row)