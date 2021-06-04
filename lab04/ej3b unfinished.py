import numpy as np
import matplotlib.pyploy as plt

datos = np.loadtxt("lab04\datos\datos3b.dat")

x = datos[0]
y = datos[1]

# y = x / (Ax + B)
# y = 1 / (A + B/x)
# log(y) = log(1 / (A + B/x))
# log(y) = log(1) - log(A + B/x)
# log(y) = - log(A + B/x)
# e**log(y) = - e**(log(A + B/x)) 

