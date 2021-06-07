import ej1
import numpy as np

intervalos = [4, 10, 20]

fun = lambda x : np.exp(-x)

# Valor exacto para comparar
I_exacta = np.exp(0) - np.exp(-1)

print(f"El valor exacto de la integral es {I_exacta}")

print("Usando la regla compuesta de Simpson:")
for N in intervalos:
    I = ej1.intenumcomp(fun, 0, 1, N, "simpson")
    err_exacto = np.abs(I - I_exacta)
    print(f"Con {N} subintervalos el error absoluto es: {err_exacto}")

print("Usando la regla compuesta del trapecio:")
for N in intervalos:
    I = ej1.intenumcomp(fun, 0, 1, N, "trapecio")
    err_exacto = np.abs(I - I_exacta)
    print(f"Con {N} subintervalos el error absoluto es: {err_exacto}")

print("Usando la regla compuesta del punto medio:")
for N in intervalos:
    I = ej1.intenumcomp(fun, 0, 1, N, "pm")
    err_exacto = np.abs(I - I_exacta)
    print(f"Con {N} subintervalos el error absoluto es: {err_exacto}")