import ej2
import ej3
import matplotlib.pyplot as plt

# Defino esta función para graficar el polinomio porque la del ej3 también devuelve
# la derivada. Hay otras maneras de hacerlo, pero esta me resultó más cómoda.
def polinomio_grafico(x):
    return x**3 + x - 5

def graficar():
    _, _, hxs, hys = ej2.busqueda_ceros(ej3.polinomio, -2, 4, 1e-6, 15)
    # Voy a considerar el método de la secante como el que consigue la mejor solución
    # porque obtiene el número más cercano al 0 y lo hace en menos iteraciones
    # Creo un array de puntos x en [-2, 4]
    x = []
    for i in range(-200, 400):
        x.append(i*0.01)
    y = [polinomio_grafico(xi) for xi in x]
    # Grafico el polinomio
    plt.plot(x, y, label="Polinomio")
    # Grafico los puntos visitados por el método de la secante
    plt.plot(hxs, hys, "o", label="Puntos visitados")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    graficar_()