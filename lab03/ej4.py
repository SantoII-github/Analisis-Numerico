from math import cos, pi
import matplotlib.pyplot as plt
import ej2

f = lambda x : 1 / (1 + 25*x**2)

h = 2/199
x_plot = [-1 +h*i for i in range(200)]

f_plot = [f(x) for x in x_plot]

fig = plt.figure()
axes = []

for n in range(1, 16):
    # Interpolación de p
    x_inter_p = [2*(i-1)/n - 1 for i in range(1, n+2)]
    f_inter_p = [f(x) for x in x_inter_p]
    p_plot = ej2.inewton(x_inter_p, f_inter_p, x_plot)
    # Interpolación de q
    x_inter_q = [cos((2*i+1)/(2*n +2)*pi) for i in range(n+1)]
    f_inter_q = [f(x) for x in x_inter_q]
    q_plot = ej2.inewton(x_inter_q, f_inter_q, x_plot)

    axes.append(fig.add_subplot(5, 3, n))
    axes[-1].plot(x_plot, f_plot, "b-")
    axes[-1].plot(x_plot, p_plot, "r-")
    axes[-1].plot(x_plot, q_plot, "y-")
    axes[-1].grid()

plt.show()
    
    