# Вычисления определителя прямым ходом Гаусса
import random

def generate_matrix(rows, cols):
    return [[random.randint(0, 5) for i in range(cols)] for i in range(rows)]

def print_matrix(matrix):
    for row in matrix:
        print(row)

def gaussian_determinant(matrix):
    det = 1

    for i in range(n):
        max_row = i
        for j in range(i + 1, n):
            if abs(matrix[j][i]) > abs(matrix[max_row][i]):
                max_row = j

        if matrix[max_row][i] == 0:
            return 0

        if max_row != i:
            matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
            det *= -1

        pivot = matrix[i][i]
        det *= pivot

        for j in range(i + 1, n):
            factor = matrix[j][i] / pivot
            for k in range(i, n):
                matrix[j][k] -= factor * matrix[i][k]

    return det

n = int(input("Введите размерность квадратной матрицы: "))

matrix = generate_matrix(n, n)

print("\nСгенерированная матрица:")
print_matrix(matrix)

determinant = gaussian_determinant(matrix)
print(f"\nОпределитель матрицы: {determinant}")