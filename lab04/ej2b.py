import numpy as np
import matplotlib.pyplot as plt
import math

# Creo los puntos
x = np.linspace(0, 4*math.pi, 50)
y = [math.cos(xi) for xi in x]
y_ruido = y + np.random.randn(len(y))

# Creo los ajustes polinomiales
coefs0 = np.polyfit(x, y_ruido, 0)
coefs1 = np.polyfit(x, y_ruido, 1)
coefs2 = np.polyfit(x, y_ruido, 2)
coefs3 = np.polyfit(x, y_ruido, 3)
coefs4 = np.polyfit(x, y_ruido, 4)
coefs5 = np.polyfit(x, y_ruido, 5)

# Hago los cálculos
y_fit0 = np.polyval(coefs0, x)
y_fit1 = np.polyval(coefs1, x)
y_fit2 = np.polyval(coefs2, x)
y_fit3 = np.polyval(coefs3, x)
y_fit4 = np.polyval(coefs4, x)
y_fit5 = np.polyval(coefs5, x)

print("Suma de residuos grado 0: " + str(sum(abs(y_ruido - y_fit0))))
print("Suma de residuos grado 1: " + str(sum(abs(y_ruido - y_fit5))))
print("Suma de residuos grado 2: " + str(sum(abs(y_ruido - y_fit5))))
print("Suma de residuos grado 3: " + str(sum(abs(y_ruido - y_fit5))))
print("Suma de residuos grado 4: " + str(sum(abs(y_ruido - y_fit5))))
print("Suma de residuos grado 5: " + str(sum(abs(y_ruido - y_fit5))))


# Grafico (Porque quiero, el ejercicio no lo pide)
# plt.plot(x, y_ruido, '*', label="Puntos con ruido")
# plt.plot(x, y_fit0, label="Grado 0")
# plt.plot(x, y_fit1, label="Grado 1")
# plt.plot(x, y_fit2, label="Grado 2")
# plt.plot(x, y_fit3, label="Grado 3")
# plt.plot(x, y_fit4, label="Grado 4")
# plt.plot(x, y_fit5, label="Grado 5")
# plt.grid()
# plt.legend()
# plt.show()