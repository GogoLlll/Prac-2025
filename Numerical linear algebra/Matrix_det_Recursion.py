# Вычисления определителя рекурсивно
import random

def generate_matrix(rows, cols):
    return [[random.randint(0, 5) for i in range(cols)] for i in range(rows)]


def print_matrix(matrix):
    for row in matrix:
        print(row)


def determinant(matrix):
    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0

    for col in range(n):
        minor = [row[:col] + row[col + 1:] for row in matrix[1:]]

        minor_det = determinant(minor)
        sign = (-1) ** col

        det += matrix[0][col] * sign * minor_det

    return det

n = int(input("Введите размерность квадратной матрицы: "))

matrix = generate_matrix(n, n)

print("\nСгенерированная матрица:")
print_matrix(matrix)

determinant_value = determinant(matrix)
print(f"\nОпределитель матрицы: {determinant_value}")