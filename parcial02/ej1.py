import numpy as np
import matplotlib.pyplot as plt

def ivander(x, y, z):
    n = len(x)
    # Inicializa la matriz de Vandermonde en 0 para armarla.
    vander = np.zeros((n,n))
    # j es la fila de la matriz.
    for j in range(n):
        # i es la columna de la matriz.
        for i in range(n):
            vander[j,i] = np.power(x[j],i)
    # u son las soluciones del sistema Vu = y
    u = np.linalg.solve(vander, y)
    # Doy vuelta los coeficients para poder usarlos con polyval
    u = np.flip(u)
    z_solve = [np.polyval(u, zi) for zi in z]
    
    return z_solve

def ilagrange(x, y, z):
    if len(x) != len(y):
        print("X e Y no tienen la misma longitud.")
        return None
    n = len(x)
    w = []
    
    for z_i in z:
        w_i = 0.0
        for idx in range(n):
            l_i = 1.0
            for jdx in range(n):
                if jdx != idx:
                    l_i = l_i * ((z_i - x[jdx]) / (x[idx] - x[jdx]))
            w_i = w_i + y[idx] * l_i
        w.append(w_i)

    return w

def solveej1():
    print("Ejercicio 1:")
    x = np.linspace(0, 2*np.pi, 55)
    y = np.sin(x)
    z = np.linspace(0, 2*np.pi, 100)

    eval_vander = ivander(x,y,z)
    eval_lagrangre = ilagrange(x, y, z)

    fig, ax = plt.subplots(2, 1)

    print("Mostrando los polinomios interpolantes...")
    print("")
    ax[0].plot(z, eval_vander, label="Vandermonde")
    ax[0].plot(x, y, "*", label="Puntos a interpolar")
    ax[0].grid()
    ax[0].legend()
    ax[1].plot(z, eval_lagrangre, label="Lagrange")
    ax[1].plot(x, y, "*", label="Puntos a interpolar")
    ax[1].grid()
    ax[1].legend()

    plt.show()

if __name__ == "__main__":
    solveej1()