def inewton(x, y, z):
    # Cantidad de puntos a interpolar:
    n = len(x)

    # Armo matriz de diferencias divididas    
    matriz_coefs = [[0.0]*m for m in range(n, 0, -1)]

    # La primera columna de la matriz son los coeficientes
    for i in range(n):
            matriz_coefs[i][0] = y[i]

    # Completo la matriz
    for j in range(1, n):
        for i in range(0, n-j):
            matriz_coefs[i][j] = (matriz_coefs[i+1][j-1] - matriz_coefs[i][j-1]) / (x[i+j] - x[i])
    
    # Me quedo con los valores de la primera fila
    coefs = matriz_coefs[0]

    # Evalúo en todos los puntos
    w = [horn_newton(zj, x, coefs) for zj in z]
    return w

def horn_newton(zj, x, coefs):
    n = len(coefs)
    valor = coefs[n-1]
    for i in range(n-2, -1, -1):
        valor = coefs[i] + (zj - x[i])*valor
    
    return valor

if __name__ == "__main__":
    x = [2, 2.5, 4]
    y = [0.5, 0.4, 0.25]
    z = [3]
    print(inewton(x, y, z))