import ej1
import numpy as np

funa = lambda x : x*np.exp(-x)
a_exacta = (1-1)*np.exp(-1) - (-np.exp(-0))
# Error Compuesta Simpson:
# (b - a)/180 * h**4 * f^4(u)
# b = 1, a = 0, h = (b-a)/n, f^4(x) = (x-4)*e**(-x)
# f^4 es creciente. Como para el error tengo que usar valor absoluto, la evalúo en 0
# error <= |(b - a)/180 * h**4 * f^4(1)|

N = 0
err_a = 1
while err_a > 10**(-5):
    N = N + 1
    err_a = abs((1/180) * (1/N)**4 * (0-4)*np.exp(-0))

if N%2 != 0:
    N = N + 1

res_a = ej1.intenumcomp(funa, 0, 1, N, "simpson")

print(f"Para la función a se necesitan usar {N} subintervalos y el resultado es {res_a}")

# Para el resto de funciones hacer lo mismo reemplazando la derivada en la cota del error.
# Es lo mismo que hacerlo en lápiz y papel acotando N.