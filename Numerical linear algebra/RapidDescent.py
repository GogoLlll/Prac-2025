#Метод скорейшего спуска
import random
import time
import math

def generate_spd_matrix(n):
    A = [[random.randint(1, 5) for _ in range(n)] for _ in range(n)]

    A = [[sum(A[i][k] * A[j][k] for k in range(n)) for j in range(n)] for i in range(n)]

    for i in range(n):
        A[i][i] += n * 5

    return A

def generate_vector(n):
    return [random.randint(1, 10) for _ in range(n)]

def dot_product(v1, v2):
    return sum(v1[i] * v2[i] for i in range(len(v1)))

def matrix_vector_mult(A, x):
    return [sum(A[i][j] * x[j] for j in range(len(x))) for i in range(len(A))]

def vector_sub(v1, v2):
    return [v1[i] - v2[i] for i in range(len(v1))]

def vector_norm(v):
    return math.sqrt(sum(x ** 2 for x in v))

def steepest_descent_method(A, b, tol=1e-6, max_iter=1000):
    n = len(A)
    x = [0.0] * n
    r = vector_sub(b, matrix_vector_mult(A, x))
    iterations = 0

    while vector_norm(r) > tol and iterations < max_iter:
        Ar = matrix_vector_mult(A, r)
        alpha = dot_product(r, r) / dot_product(r, Ar)
        x = [x[i] + alpha * r[i] for i in range(n)]
        r = vector_sub(b, matrix_vector_mult(A, x))
        iterations += 1

    return x, iterations

n = int(input("Введите размерность системы: "))

A = generate_spd_matrix(n)
b = generate_vector(n)

print("\nМатрица A:")
for row in A:
    print(row)
print("\nВектор правой части b:")
print(b)

start_time = time.time()
x, iterations = steepest_descent_method(A, b)
end_time = time.time()

print("\nРешение системы (вектор x):")
print(x)
print(f"\nКоличество итераций: {iterations}")
print(f"Время выполнения: {end_time - start_time:.6f} секунд")