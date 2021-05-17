from ej1 import ilagrange
from ej2 import inewton
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

x = [-3, -2, -1, 0, 1, 2, 3]
f = [1, 2, 5, 10, 5, 2, 1]

h = 6/199
x_plot = [-3 + h*i for i in range(200)]

w_lagrange = ilagrange(x, f, x_plot)
w_newton = inewton(x, f, x_plot)
polinomio = interp1d(x, f, kind="cubic")
w_interp1d = polinomio(x_plot)

plt.plot(x_plot, w_lagrange, label="Lagrange")
plt.plot(x_plot, w_newton, label="Newton")
plt.plot(x_plot, w_interp1d, label="Spline Cúbico")
plt.plot(x, f, "o", label="Puntos de interpolación")
plt.grid()
plt.legend()
plt.show()