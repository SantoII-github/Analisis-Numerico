import numpy as np
import matplotlib.pyplot as plt

# Leo los datos que me dan
datos = np.loadtxt("lab04\datos\datos1a.dat")

# Los datos son dos columnas, las separo
x = datos[:,0]
y = datos[:,1]

# Calculo los que necesito para la matriz
m = len(x)
sum_xi = sum(x)
sum_yi = sum(y)
sum_xi2 = sum(x ** 2)
sum_xiyi = sum(x * y)

# La matriz a resolver es:
# [m      sum_xi ] [a0] = [sum_yi] 
# [sum_xi sum_xi2] [a1] = [sum_xiyi]

# Por suerte, el teórico tiene la fórmula para cada coeficiente
a0 = (sum_xi2 * sum_yi - sum_xiyi * sum_xi) / (m * sum_xi2 - sum_xi ** 2)
a1 = (m * sum_xiyi - sum_xi * sum_yi) / (m * sum_xi2 - sum_xi ** 2)

# Función para evaluar la recta
def eval(x):
    return a1*x + a0

# 100 puntos para evaluar la recta y graficarla
x_graph = np.linspace(0, 5, 100)
y_graph = eval(x_graph)

# Grafico

plt.plot(x_graph, y_graph)
plt.plot(x, y, '*')
plt.grid()
plt.show()