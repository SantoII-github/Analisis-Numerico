from scipy import linalg
import numpy as np
from ej1 import soltrinf, soltrsup

def sollu(A, b):
    # A = P L U
    P, L, U = linalg.lu(A)
    
    # Ax = b -> PLUx = b
    # LUx = P^T b = y
    # Lz = y
    # Ux = z

    y = P.T @ b
    z = soltrinf(L, y)
    x = soltrsup(U, z)

    return x

if __name__ == "__main__":
    A = np.random.rand(4,4)
    x = np.random.rand(4)
    b = A @ x
    x_sol = sollu( A, b )
    print(b)
    print(A @ x_sol)
    print(x_sol)
    print(x)
