from scipy import integrate
import numpy as np
import math

funa = lambda  x : np.exp(-x**2)
res_a = integrate.quad(funa, -np.inf, np.inf)
print(f"El resultado para la función a es {res_a[0]} con error aproximado {res_a[1]}")

funb = lambda  x : x**2 * math.log(x + (x**2 + 1)**(1/2))
res_b = integrate.quad(funb, 0, 2)
print(f"El resultado para la función b es {res_b[0]} con error aproximado {res_b[1]}")