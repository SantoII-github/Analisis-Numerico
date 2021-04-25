import ej2
# Implementación del algoritmo de Horner sacada del lab01
# coeficientes = [1, 2, 3] ---> x^2 + 2x + 3
def horn(valor, coeficientes):
    n = len(coeficientes)
    b = coeficientes[0]
    for i in range (1, n):
        b = coeficientes[i] + b * valor
    return b

def polinomio(x):
    return horn(x, [1, 1, -5]), horn(x, [3, 1])

if __name__ == "__main__":
    ej2.busqueda_ceros(polinomio, 10.0, -10.0, 1e-6, 15)
