from ej3 import rnewton

def aprox_cubicroot_a(a):
    assert(a>0)
    def fun(x):
        function = x**3 - a
        derivative = 3*(x**2)
        return function, derivative
    
    hx, _ = rnewton(fun, a-1, 1e-6, 100)
    return hx[-1]

print(f"La aproximación de a**1/3 es: {aprox_cubicroot_a(8)}")

