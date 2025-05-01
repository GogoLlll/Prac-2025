# Метод прогонки
import random

def generate_tridiagonal_matrix(n):
    main_diag = [random.randint(2, 5) for _ in range(n)]

    upper_diag = [random.randint(1, 3) for _ in range(n - 1)]

    lower_diag = [random.randint(1, 3) for _ in range(n - 1)]

    matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][i] = main_diag[i]
        if i < n - 1:
            matrix[i][i + 1] = upper_diag[i]
            matrix[i + 1][i] = lower_diag[i]

    return matrix

def generate_vector(n):
    return [random.randint(1, 10) for _ in range(n)]

def print_matrix(matrix):
    for row in matrix:
        print(row)

def thomas_algorithm(A, b):
    n = len(A)

    a = [0] * n
    b_vec = [0] * n
    c = [0] * n
    d = b.copy()

    for i in range(n):
        b_vec[i] = A[i][i]
        if i > 0:
            a[i] = A[i][i - 1]
        if i < n - 1:
            c[i] = A[i][i + 1]

    for i in range(1, n):
        m = a[i] / b_vec[i - 1]
        b_vec[i] = b_vec[i] - m * c[i - 1]
        d[i] = d[i] - m * d[i - 1]

    x = [0] * n
    x[-1] = d[-1] / b_vec[-1]
    for i in range(n - 2, -1, -1):
        x[i] = (d[i] - c[i] * x[i + 1]) / b_vec[i]

    return x

n = int(input("Введите размерность системы: "))

A = generate_tridiagonal_matrix(n)
b = generate_vector(n)

print("\nТрёхдиагональная матрица A:")
print_matrix(A)
print("\nВектор правой части b:")
print(b)

x = thomas_algorithm(A, b)

print("\nРешение системы (вектор x):")
print(x)