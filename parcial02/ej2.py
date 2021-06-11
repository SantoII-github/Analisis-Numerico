import numpy as np
from scipy import linalg

def sollu(A, b):
    P, L, U = linalg.lu(A)

    y = P.T @ b
    z = soltrinf(L, y)
    x = soltrsup(U, z)

    return x

def soltrinf(A, b):
    if np.linalg.det(A) == 0:
        print("La matriz es singular")
        return None
    
    n = A.shape[0]
    x = np.zeros(n)

    for i in range(n):
        sumatoria = 0
        for j in range(i):
            sumatoria += A[i,j] * x[j]
        
        x[i] = (b[i] - sumatoria)/A[i,i]
    
    return x

def soltrsup(A, b):
    if np.linalg.det(A) == 0:
       print("La matriz es singular")
       return None

    n = A.shape[0]
    x = np.zeros(n)

    for i in range(n-1, -1, -1):
        sumatoria = 0
        for j in range(i, n):
            sumatoria += A[i,j] * x[j]
        
        x[i] = (b[i] - sumatoria) / A[i,i]
    
    return x

def solveej2():
    print("Ejercicio 2:")
    # Inciso 1
    # Calculé los coeficientes en papel.
    K = np.array([[ 30.0, -20.0,   0.0],\
                  [-20.0,  30.0, -10.0],\
                  [  0.0, -10.0,  10.0]])

    w = np.array([19.6, 29.4, 24.5])
    x = sollu(K, w)
    print("-- Inciso 1 --")
    print("Las soluciones del sistema de masas Kx = w son:")
    print(f" x1 = {x[0]}")
    print(f" x2 = {x[1]}")
    print(f" x3 = {x[2]}")

    # Inciso 2
    P, L, U = linalg.lu(K)
    A = L @ U
    # Base canónica
    e1 = np.array([1,0,0])
    e2 = np.array([0,1,0])
    e3 = np.array([0,0,1])
    inversa = np.array([np.linalg.solve(A,e1),\
                        np.linalg.solve(A,e2),\
                        np.linalg.solve(A,e3)])
    
    print("-- Inciso 2 --")
    print("La inversa de la matriz K es:")
    print(inversa)


if __name__ == "__main__":
    solveej2()