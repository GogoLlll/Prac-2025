# Генератор матриц и вектора
import random

def generate_matrix(rows, cols):
    return [[random.randint(0, 5) for _ in range(cols)] for _ in range(rows)]

def generate_vector(size):
    return [random.randint(0, 5) for _ in range(size)]

rows = int(input("Введите количество строк: "))
cols = int(input("Введите количество столбцов: "))
vector_size = int(input("Введите размер вектора: "))

matrix = generate_matrix(rows, cols)
vector = generate_vector(vector_size)

print("\nСгенерированная матрица:")
for row in matrix:
    print(row)

print("\nСгенерированный вектор:")
print(vector)