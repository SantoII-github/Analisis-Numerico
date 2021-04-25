from ej1 import rbisec
from ej3 import rnewton
from ej5 import ripf
import math
import matplotlib.pyplot as plt
import numpy

def lab2ej7bisec(x):
    fun_aux = lambda y : y - math.exp(-(1-x*y)**2)
    hy, hu = rbisec(fun_aux, [0.0, 2.0], 1e-6, 100)
    y = hy[-1]
    return y

def lab2ej7newton(x):
    fun_aux = lambda y : (y - math.exp(-(1-x*y)**2), \
        1 - 2*x*(1 - x*y) * math.exp(-(1-x*y)**2))
    hy, hu = rnewton(fun_aux, 1.0, 1e-6, 100)
    y = hy[-1]
    return y

def lab2ej7ipf(x):
    fun_aux = lambda y : math.exp(-(1-x*y)**2)
    hy = ripf(fun_aux, 1.0, 1e-6, 100)
    y = hy[-1]
    return y

# Gráficos
# Creo los ejes
fig, ax = plt.subplots(3, 1)
# Creo los puntos del intervalo [0, 1.5]
x = numpy.linspace(0, 1.5, 100)

# Calculo los resultados de las funciones en cada punto
y_bisec = [lab2ej7bisec(xi) for xi in x]
y_newton = [lab2ej7newton(xi) for xi in x]
y_ipf = [lab2ej7ipf(xi) for xi in x]

# Hago los gráficos
ax[0].plot(x, y_bisec)
ax[1].plot(x, y_newton)
ax[2].plot(x, y_ipf)
plt.show()

plt.plot(x,y_ipf,'g')
plt.plot(x,y_bisec,'--r')
plt.plot(x,y_newton,'ob')
plt.show()