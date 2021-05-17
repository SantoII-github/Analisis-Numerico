import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

datos = np.loadtxt("lab03\datos_aeroCBA.dat")

años = datos[:,0]
temps = datos[:,1]

not_nan = ~np.isnan(temps)
años_interp = años[not_nan]
temps_interp = temps[not_nan]

polinomio = interp1d(años_interp, temps_interp, kind="cubic", fill_value="extrapolate")

años_plot = np.arange(1957, 2018)
temps_plot = polinomio(años_plot)

plt.plot(años_plot, temps_plot)
plt.plot(años_interp, temps_interp, "o")
plt.grid()
plt.show()