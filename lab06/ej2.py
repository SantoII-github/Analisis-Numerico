import numpy as np
import ej1
from scipy import linalg

# Aplica el método de eliminación Gaussiana.
# Devuelve [U, y] con U ∈ R^nxn triangular superior y b ∈ R^n
def egauss(A, b):
    if np.linalg.det(A) == 0:
        print("La matriz es singular")
        return None
    
    # n = Longitud de una fila de la matriz
    n = A.shape[0]
    U = A.copy()
    y = b.copy()

    for k in range(n-1):
        for i in range(k+1,n):
            if U[k,k] == 0:
                print('El elemento a_kk es igual a cero.')
                return None

            m = U[i,k]/U[k,k]

            for j in range(k, n):
                U[i,j] = U[i,j] - m*U[k,j]
            y[i] = y[i] - m*y[k]
        
    return U, y

def soleg(A,b):
    U, y = egauss(A,b)
    x = linalg.solve(U,y)
    return x

# Es importante que la matriz que pasamos al método contenga floats.
# Si tiene únicamente ints se introducen errores numéricos.
if __name__ == "__main__":
    A = np.random.rand(4,4)
    x = np.random.rand(4)
    b = A @ x
    x_sol = soleg( A, b )
    print(b)
    print(A @ x_sol)
    print(x_sol)
    print(x)

