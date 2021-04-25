# rsecante implementa el método de la secante
# Entradas:
# -fun, función que dado x retorna f(x)
# -x0 e x1, puntos iniciales
# -err, tolerancia del error
# -mit, número máximo de iteraciones permitidas
# Salidas:
# hx, historial de puntos medios
# hf, historial de los respectivos valores funcionales

def rsecante(fun, x0, x1, err, mit):
    fx0 = fun(x0)
    fx1 = fun(x1)
    hx = [x1]
    hf = [fx1]

    for _ in range(mit):
        s = (x1 - x0)/(fx1 -fx0)    
        x1 = x0                     
        fx1 = fx0
        x0 = x0 - fx0 * s           
        fx0 = fun(x0)
        hx.append(x0)
        hf.append(fx0)
        if abs(x1 - x0) < err or abs(fx0) < err:
            break
    return hx, hf
