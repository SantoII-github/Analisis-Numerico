from ej1 import simpson
import numpy as np
import time

def simpson_simple(fun,a,b):
	return simpson(fun,a,b,2)

def simpson_adap(fun,a,b,err):
    c = (a+b)/2
    q = simpson_simple(fun,a,b)
    q1 = simpson_simple(fun,a,c)
    q2 = simpson_simple(fun,c,b)
    if abs(q-q1-q2) < 15*err:
        I = q1 + q2
    else: 
        q1 = simpson_adap(fun, a, c, err/2)
        q2 = simpson_adap(fun, c, b, err/2)
        I = q1 + q2
    return I

fun = lambda x : x*np.exp(-x**2)
err = 1e-15
I_exacta = 0.5*(1-np.exp(-1))

start = time.time()

I_adaptativa = simpson_adap(fun,0,1,err)

print(f"Simpson adaptativo demoró {time.time()-start} y calculó {I_adaptativa}")

cota_d4f = 156
N_simpson = int(np.ceil((cota_d4f/(err*180))**(1/4)))

start = time.time()

I_compuesta = simpson(fun, 0, 1, N_simpson)

print(f"Simpson compuesta demoró {time.time()-start} y calculó {I_compuesta}")