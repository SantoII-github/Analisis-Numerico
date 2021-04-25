# Ejercicio 5
# Implementar método de iteración de punto fijo de ɸ : R -> R
# partiendo de un punto inicial x0
# Entrada
# -fun, función que dado x retorna ɸ(x)
# -x0, un punto en R
# -err, tolerancia deseada del error
# -mit, número máximo de iteraciones
# El algoritmo finaliza en la k-ésima iteración si |xk - x(k-1)| < err
# o si k >= mit.
# Salida
# -hx, historial de puntos generados

def ripf(fun, x0, err, mit):
    hx = [x0]
    for _ in range(mit):
        xk = fun(x0)
        hx.append(xk)
        if abs(xk - x0) < err:
            print("Se encontró el punto fijo.")
            return hx
        
        x0 = xk
    return hx
