# Метод Бисекций
def bisection_method(f, a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        raise ValueError("Функция должна иметь разные знаки на концах интервала [a, b].")

    iterations = 0
    while (b - a) / 2 > tol and iterations < max_iter:
        c = (a + b) / 2
        if f(c) == 0:
            return c, iterations
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        iterations += 1

    return (a + b) / 2, iterations

def f(x):
    return x ** 3 - x - 2

a = 1
b = 2
root, iterations = bisection_method(f, a, b)

print(f"Найденный корень: {root}")
print(f"Количество итераций: {iterations}")