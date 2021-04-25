from ej5 import ripf
import math

# Usar la fórmula x(n+1) = 2^xn para resolver la ecuación 2x = 2^x
# Utilizar la función del ejercicio anterior para investigar si converge.
# En caso de converger estudiar hace que valores lo hace para distintos x0
# Tomar un número máximo de 100 iteraciones y un error menor a 1e-5
# Para que el algoritmo converga el valor absoluto de la función que se usa para
# la iteración debe ser menor a 1 en el intervalo.
# La derivada de 2^x -2x es ln(2)*2^x-2,
# entonces converge para 0.52 < x0 < 2.11

def fun_lab2ej6(x):
    return math.pow(2, x)/2

hx = ripf(fun_lab2ej6(x), 1.99999, 1e-5, 100)
print(f"El valor al que converge es: {hx[-1]}")

# Converge a 1 para casi todos los valores de x0 en el intervalo, 
# para x0 > 1.99999 converge a 2. 

# Punto fijo resuelve una ecuación del tipo f(x) = x