from ej2 import soleg
from ej3 import sollu
import numpy as np

A = np.array([[4., -1.,  0., -1.,  0.,  0.],\
              [-1., 4., -1.,  0., -1.,  0.],\
              [0., -1.,  4.,  0.,  0., -1.],\
              [-1., 0.,  0.,  4., -1.,  0.],\
              [0., -1.,  0., -1.,  4., -1.],\
              [0.,  0., -1.,  0., -1.,  4.]])

b1 = np.array([1.,1.,1.,0.,0.,0.])
b2 = np.array([1.,1.,1.,1.,1.,1.])

print("Solución b1 con:")
print(f"Eliminación Gaussiana: {soleg(A, b1)}")
print(f"Descomposición LU: {sollu(A, b1)}")

print("Solución b2 con:")
print(f"Eliminación Gaussiana: {soleg(A, b2)}")
print(f"Descomposición LU: {sollu(A, b2)}")