from ej1 import rbisec
import math
import numpy
import matplotlib.pyplot as plt

# Ejercicio 2, inciso a)
# Menor solución positiva de la ecuación 2x = tan(x) con error menor a
# 10^-5 en menos de 100 iteraciones. ¿Cuántas iteraciones son necesarias
# cuando comenzamos con el intervalo [0.8, 1.4]?

def fun_lab2ej2a(x):
    return math.tan(x) - 2*x

hx, hy = rbisec(fun_lab2ej2a, [0.8, 1.4], 1e-5, 100)
print(f"La cantidad de iteraciones para la ecuación 2x = tan(x) fue: {len(hx)}")

# inciso b)
# Aproximación a √3 con un error meno a 1e-5 considerando la función x^2-3

def fun_lab2ej2b(x):
    return x**2 - 3

hx, hf = rbisec(fun_lab2ej2b, [0, 2], 1e-5, 100)
print(f"La aproximación es √3 = {hx[-1]}")

# inciso c)
# Graficar conjuntamente f y los pares (x_k, f(x_k)) para las dos funciones
# anteriores y con al menos dos intervalos iniciales distintos para cada una

def eval_function_in_points(fun, points):
    evals = []
    for index in range(0, len(points)):
        evals.append(fun(points[index]))
    return evals

# Gráfico de x^2 - 3 con intervalo [0, 2]
fig, ax = plt.subplots(2, 2)

# Gráfico de historial de puntos
ax[0][0].set_title("ej2b, [0, 2]")
ax[0][0].plot(hx, hf, 'o')
# Lista de 21 puntos equiespaciados entre 0 y 2 y sus valores
pts = numpy.linspace(0, 2, 21)
evals = eval_function_in_points(fun_lab2ej2b, pts)
# Graficar puntos en X y evaluaciones en Y
ax[0][0].plot(pts, evals)

# Gráfico de x^2 -3 con intervalo [1, 3]
hx1, hf1 = rbisec(fun_lab2ej2b, [1, 3], 1e-5, 100)
ax[0][1].set_title("ej2b, [1, 3]")
ax[0][1].plot(hx1, hf1, 'x')
pts1 = numpy.linspace(1, 3, 21)
evals1 = eval_function_in_points(fun_lab2ej2b, pts1)
ax[0][1].plot(pts1, evals1)

# Gráfico de 2x = tan(x) con intervalo [0.8, 1.4]
hx2, hf2 = rbisec(fun_lab2ej2a, [0.8, 1.4], 1e-5, 100)
ax[1][0].set_title("ej2a, [0.8, 1.4]")
ax[1][0].plot(hx2, hf2, "o")
pts2 = numpy.linspace(0.8, 1.4, 21)
evals2 = eval_function_in_points(fun_lab2ej2a, pts2)
ax[1][0].plot(pts2, evals2)

# Gráfico de 2x = tan(x) con intervalo [0, 2]
hx3, hf3, = rbisec(fun_lab2ej2a, [1, 1.5], 1e-5, 100)
ax[1][1].set_title("ej2a, [1, 1.5]")
ax[1][1].plot(hx3, hf3, "x")
pts3 = numpy.linspace(1, 1.5, 21)
evals3 = eval_function_in_points(fun_lab2ej2a, pts3)
ax[1][1].plot(pts3, evals3)

# Mostrar gráficos
plt.show()

