def f(x):
    return (x**2 + 1)**0.5 - 1

def g(x):
    return x**2/(((x**2 + 1)**0.5)+1)

# sqrt(x^2 + 1) - 1
# sqrt(x^2 + 1) - 1 * (sqrt(x^2 + 1) + 1)/((sqrt(x^2 + 1) + 1))
# (sqrt(x^2 + 1)^2 - 1^2) / ((sqrt(x^2 + 1) + 1))
# (x^2 + 1 - 1) / ((sqrt(x^2 + 1) + 1))
#  x^2 / ((sqrt(x^2 + 1) + 1))

def main():
    for i in range(20):
        x = 8**-i
        print(f"f(x) = {f(x)}, g(x) = {g(x)}")

if __name__ == '__main__':
    main()

#Las funciones no devuelven los mismos resultados porque se pierden números significativos en la resta de la expresión original.
#La función g(x) es más confiable que la función f(x)