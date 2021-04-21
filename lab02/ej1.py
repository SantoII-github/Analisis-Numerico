# Ejercicio 1
# Busca una raíz de la función fun mediante el método de bisección.
# Entradas:
# - fun: Una función de una variable que devuelva un número
# - I: Una lista que represente un intervalo: [a, b]
# - err: Una tolerancia para considerar una evaluación como cero
# - mit: Cantidad máxima de iteraciones de bisección
# Salidas:
# - hx: Lista de puntos medios visitados
# - hf: Lista de evaluaciones de esos puntos medios

def rbisec(fun, I, err, mit):
    # I es una lista de dos valores que representa un intervalo
    a = I[0]    # Inicio del intervalo
    b = I[1]    # Final del intervalo

    # Creo las listas que voy a devolver
    hx = []
    hf = []

    # Aseguro que se cumplan las hipótesis del método

    if fun(a) * fun(b) >= 0:
        print("Los extremos de la función tienen el mismo signo.")
        return hx, hf
    
    if a >= b:
        print("Los extremos del intervalo son iguales o no están ordenados.")
        return hx, hf
    
    for _ in range(mit):
        # Calculo c y f(c)
        c =  a + (b - a)/2  
        fun_c = fun(c)

        # Los agrego a las listas que devuelvo
        hx.append(c)
        hf.append(fun_c)

        # Vemos si llegamos a una raíz
        if abs(fun_c) < err:
            print("Se encontró la raíz.")
            break

        # Parte principal del algoritmo

        if fun(a) * fun_c < 0:
            b = c
        else: 
            a = c
    
    return hx, hf
