import matplotlib.pyplot as plt
import ej2

def f(z):
    return 1/z

if __name__ == "__main__":
    # zj y f(zj) para graficar 1/x
    zj = [24/25 +j/25 for j in range(1, 102)]
    f_zj = [f(z) for z in zj]
    # Los puntos en los que quiero interpolar
    i = [1, 2, 3, 4, 5]
    f_i = [f(j) for j in i]
    # Valor del polinomio interpolante en todos los zj
    w = ej2.inewton(i, f_i, zj)

    plt.plot(zj, f_zj, "r-", label="1/x")
    plt.plot(zj, w, label="Polinomio Interpolante de Newton")
    plt.plot(i, f_i, "bo", label="Puntos de Interpolación")
    plt.legend()
    plt.grid()
    plt.show()