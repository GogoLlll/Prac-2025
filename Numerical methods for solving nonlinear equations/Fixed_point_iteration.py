# Метод простой итерации
def simple_iteration_method(phi, x0, tol=1e-6, max_iter=1000):
    x = x0
    iterations = 0

    while iterations < max_iter:
        x_new = phi(x)
        if abs(x_new - x) < tol:
            return x_new, iterations

        x = x_new
        iterations += 1

    return x, iterations

def phi(x):
    return (x + 2) ** (1 / 3)

x0 = 1.5

root, iterations = simple_iteration_method(phi, x0)

print(f"Найденный корень: {root}")
print(f"Количество итераций: {iterations}")