import ej5
import numpy as np

A1 = np.array([[3.,1,1],[2,6,1],[1,1,4]])
b1 = np.array([5.,9,6])
tol1 = 10**(-11)
A2 = np.array([[5.,7,6,5],[7,10,8,7],[6,8,10,9],[5,7,9,10]])
b2 = np.array([23.,32,33,31])
tol2 = 10**(-4)

x1j = ej5.jacobi(A1, b1, tol1, 100)
x1g = ej5.gseidel(A1, b1, tol1, 100)
print("Punto 1)")
print(f"Jacobi necesita {x1j[1]} iteraciones")
print(f"Gauss-Seidel necesita {x1g[1]} iteraciones")
print(f"{x1j[0]}, {x1g[0]}")

x2j = ej5.jacobi(A2, b2, tol2, 1000)
x2g = ej5.gseidel(A2, b2, tol2, 10000)
print("Punto 1)")
print(f"Jacobi necesita {x2j[1]} iteraciones")
print(f"Gauss-Seidel necesita {x2g[1]} iteraciones")
print(f"{x2j[0]}, {x2g[0]}")

# Jacobi diverge para el inciso 2, y Gseidel lo hace en 1215 iteraciones.