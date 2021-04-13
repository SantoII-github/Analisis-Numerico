def mala(a, b, c):
    # ax^2 + bx + c
    discriminante = b**2 - 4 * a * c
    if discriminante < 0:
        print("El polinomio no tiene raíces reales.")
        return []
    else:
        x_1 = (-b + (discriminante)**0.5)/(2.0*a)
        x_2 = (-b - (discriminante)**0.5)/(2.0*a)
        return [x_1, x_2]

def buena(a, b, c):
    # ax^2 + bx + c
    discriminante = b**2 -4 * a * c
    if discriminante < 0:
        print("El polinomio no tiene raíces reales.")
        return []
    else:
        if b >= 0:                              # Dependiendo del signo de b elijo que raíz calcular primero para evitar unar esta de números muy cercanos.
            x_1 = (-b - (discriminante)**0.5)/(2.0*a)
        else:
            x_1 = (-b + (discriminante)**0.5)/(2.0*a)
        x_2 = c / (a * x_1)                     # Teniendo la primera raíz ahora puedo usar que x_1*x_2 = c/a para calcular la segunda. También podría haber usado x_1 + x_2 = -b/a
        return [x_1, x_2]


print("Resultado de la función mala: " + str(mala(1, 1e10, 1)))
print("Resultado de la función buena: " + str(buena(1, 1e10, 1)))
