from ej5 import ripf

# Usar la fórmula x(n+1) = 2^xn para resolver la ecuación 2x = 2^x
# Utilizar la función del ejercicio anterior para investigar si converge.
# En caso de converger estudiar hace que valores lo hace para distintos x0
# Tomar un número máximo de 100 iteraciones y un error menor a 1e-5

hx = ripf(fun_lab2ej6, 3, 1e-5, 100)

