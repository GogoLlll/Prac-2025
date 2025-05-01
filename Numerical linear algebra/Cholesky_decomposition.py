# Разложение Холецкого
import random
import math

def generate_matrix(n):
    A = [[random.randint(1, 5) for _ in range(n)] for _ in range(n)]
    A = [[sum(A[i][k] * A[j][k] for k in range(n)) for j in range(n)] for i in range(n)]

    for i in range(n):
        A[i][i] += n * 5

    return A

def print_matrix(matrix):
    for row in matrix:
        print(row)

def cholesky_decomposition(A):
    n = len(A)
    L = [[0.0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1):
            s = sum(L[i][k] * L[j][k] for k in range(j))
            if i == j:
                L[i][j] = math.sqrt(A[i][i] - s)
            else:
                L[i][j] = (A[i][j] - s) / L[j][j]

    return L

def determinant_cholesky(L):
    n = len(L)
    det = 1.0
    for i in range(n):
        det *= L[i][i]
    return det ** 2

n = int(input("Введите размерность квадратной матрицы: "))

matrix = generate_matrix(n)

print("\nСгенерированная матрица:")
print_matrix(matrix)

L = cholesky_decomposition(matrix)
determinant_value = determinant_cholesky(L)

print("\nНижняя треугольная матрица L:")
print_matrix(L)
print(f"\nОпределитель матрицы: {determinant_value}")