import numpy as np

# Resuelve el sistema Ax = b con A matriz triangular inferior y b ∈ R^n
# Devuelve la solución x
def soltrinf(A, b):
    if np.linalg.det(A) == 0:
        print("La matriz es singular")
        return None
    
    # n = longitud del arreglo en una dirección
    n = A.shape[0]
    # Creo el arreglo en el que devolveré la solución y lo inicializo en 0.
    x = np.zeros(n)

    for i in range(n):
        sumatoria = 0
        # La sumatoria empieza en 0 en lugar de 1 como el pseudocódigo
        # por los índices de los arreglos.
        for j in range(i):
            sumatoria += A[i,j] * x[j]
        
        x[i] = (b[i] - sumatoria)/A[i,i]
    
    return x

# Resuelve el sistema Ax = b con A matriz triangular superior y b ∈ R^n
# Devuelve la solución x

def soltrsup(A, b):
    if np.linalg.det(A) == 0:
       print("La matriz es singular")
       return None

    n = A.shape[0]
    x = np.zeros(n)

    # n-1 downto 1
    for i in range(n-1, -1, -1):
        sumatoria = 0
        # i+1 to n-1
        for j in range(i, n):
            sumatoria += A[i,j] * x[j]
        
        x[i] = (b[i] - sumatoria) / A[i,i]
    
    return x


if __name__ == "__main__":
    Au = np.triu(np.random.rand(4,4))
    Al = np.tril(np.random.rand(4,4))
    x = np.random.rand(4)
    bu = Au @ x
    bl = Al @ x
    print(soltrsup(Au, bu), x)
    print(soltrinf(Al, bl), x)