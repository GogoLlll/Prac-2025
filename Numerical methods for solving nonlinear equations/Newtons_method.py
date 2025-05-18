# Метод Ньютона
def newton_method(f, df, x0, tol=1e-6, max_iter=1000):
    x = x0
    iterations = 0

    while iterations < max_iter:
        f_x = f(x)
        df_x = df(x)

        if abs(f_x) < tol:
            return x, iterations

        if df_x == 0:
            raise ValueError("Производная равна нулю. Метод Ньютона не может быть применён.")

        x_new = x - f_x / df_x
        if abs(x_new - x) < tol:
            return x_new, iterations

        x = x_new
        iterations += 1

    return x, iterations

def f(x):
    return x ** 3 - x - 2

def df(x):
    return 3 * x ** 2 - 1

x0 = 1.5

root, iterations = newton_method(f, df, x0)

print(f"Найденный корень: {root}")
print(f"Количество итераций: {iterations}")