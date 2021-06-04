import numpy as np
import matplotlib.pyplot as plt

# Creo los 20 puntos y los evalúo en la recta.
x = np.linspace(0, 10, 20)
y = (3/4)*x - (1/2)

y_ruido = y + np.random.randn(len(y))

# Consigo los coeficientes de una aproximación por cuadrados mínimos de grado 1
coefs = np.polyfit(x, y_ruido, 1)

# Evalúo el polinomio generado por polyfit en mis puntos x.
y_fit = np.polyval(coefs, x)

# Grafico
plt.plot(x, y, label="Recta Original")
plt.plot(x, y_ruido, 'o', label="Puntos con ruido")
plt.plot(x, y_fit, label="Recta Ajustada")
plt.grid()
plt.legend()
plt.show()