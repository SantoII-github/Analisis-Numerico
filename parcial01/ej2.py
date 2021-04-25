import ej1

# Función del método de Newton, sacada de los ejercicios de lab02
def rnewton(fun, x0, err, mit):
    hx = []
    hf = []
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

# Implementar función busqueda_ceros con las mismas entradas que el ejercicio
# anterior. Tiene que aplicar los métodos de Newton (con punto inicial x0) y
# de la secante sobre la función fun. Debe imprimir en pantalla los ceros
# encontrados con ambos métodos, la cantidad de iteraciones que le toma a 
# cada método para llegar al cero y debe retornar el punto para el cual
# el valor absoluto de la función es el menor. 

def busqueda_ceros(fun, x0, x1, err, mit):
    # Defino una función auxiliar sin la derivada para el método de la secante
    def fun_aux(x):
        res, _ = fun(x)
        return res
    # Calculo los valores que necesito
    hx_newton, hy_newton = rnewton(fun, x0, err, mit)
    hx_secante, hy_secante = ej1.rsecante(fun_aux, x0, x1, err, mit)
    
    # Imprimo en pantalla lo que pide el ejercicio
    print("--- Método de Newton ---")
    print(f"Cero encontrado: {hx_newton[-1]}")
    print(f"Cantidad de iteraciones: {len(hx_newton)}\n")
    print("--- Método de la secante ---")
    print(f"Cero encontrado: {hx_secante[-1]}")
    print(f"Cantidad de iteraciones: {len(hx_secante)}\n")
    if abs(hy_newton[-1]) < abs(hy_secante[-1]):
        print("El método de newton da el cero más cercano")
    if abs(hy_newton[-1]) > abs(hy_secante[-1]):
        print("El método de la secante da el cero más cercano")
    if abs(hy_newton[-1]) == abs(hy_secante[-1]):
        print("En contra de toda expectativa, los métodos llegaron a exactamente el mismo número")

    return hx_newton, hy_newton, hx_secante, hy_secante
