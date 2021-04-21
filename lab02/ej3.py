# Ejercicio 3
# Implementar el método de Newton para hallar una raíz de f : R -> R
# partiendo de x0
# Entradas
# - fun, función que dado x retorna f(x) y f'(x)
# - x0, punto inicial en R
# - err, tolerancia deseada del error
# - mit, número máximo de iteraciones permitidas
# El algoritmo debe finalizar en la k-esima iteración si se cumple
# algunas de las siguientes condiciones:
# |xk -x(k-1)|/|xk| < err, |f(xk)| < err, k >= mit
# Salidas
# - hx, historial de puntos generados
# - hf, historial de evaluación de la función en los puntos

def rnewton(fun, x0, err, mit):
    # Creo las listas que devolverá la función
    hx = []
    hf = []
    # fun[0] = f(x), fun[1] = f'(x)
    # Guardo la función y su derivada en variables
    f, df = fun(x0)

    for _ in range(mit):
        if df == 0:
            print("La derivada en el punto es nula. Lleva a dividir por cero")
            break

        xk = x0 - f/df
        f, df = fun(xk)

        hx.append(xk)
        hf.append(f)

        if abs(xk - x0)/abs(xk) < err or abs(f) < err:
            break
            
        x0 = xk
    return hx, hf    
    
def test(x):
    function = x**2
    derivative = 2*x
    return function, derivative

