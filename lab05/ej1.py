import numpy as np

def intenumcomp(fun, a, b, N, regla):
    if regla == "trapecio":
        return trapecio(fun, a, b, N)
    elif regla == "pm":
        return pm(fun, a, b, N)
    elif regla == "simpson":
        return simpson(fun, a, b, N)
    else:
        print("Regla Inválida")

def pm(fun, a, b, N):
    if N%2 != 0:
	    print("N debe ser par")
	    return None

    h = (b-a)/(N+2)
    n = (N//2)+1
    sum = 0
    for j in range(0, n):
        sum += fun((a+(2*j+1)*h))
    I = 2*h*sum

    return I

def trapecio(fun, a, b, N):
    # I = (h/2) + 2 * sum(f(xj) + f(b))
    h = (b-a)/N
    # No incluyo a + 0*h y a + N*h porque 
    # son a y b respectivamente, que no van en la sumatoria.
    xj = np.array([a + j*h for j in range(1, N)])
    sumfunxj = sum(fun(xj))
    I = (h/2)*(fun(a) + 2*sumfunxj + fun(b))
    return I

def simpson(fun, a, b, N):
    if N%2 != 0:
	    print("N debe ser par")
	    return None
    
    h = (b-a)/N
    x = np.linspace(a, b, N+1)
    f = np.array([fun(xi) for xi in x])
    fn = f[-1]
    # Cambio la forma de f para que los pares estén en la primer columna y
    # los impares en la segunda.
    f = np.reshape(f[:-1],(-1,2))
    f0 = f[0,0]
    f_pares = f[1:,0]
    f_impares = f[:,1]
    I = (h/3)*(f0 + 2*np.sum(f_pares) + 4*np.sum(f_impares) + fn)
    return I

