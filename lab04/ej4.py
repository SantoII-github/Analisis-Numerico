import numpy as np
import matplotlib.pyplot as plt

y = np.loadtxt("lab04\datos\covid_italia.csv", delimiter=",", usecols=1)
x = np.arange(len(y))

# y = a*e**(bx)
# log(y) = log(a*e**(bx))
# log(y) = log(a) + b*x*log(e)
# log(y) = log(a) + b*x
#
# y_p = log(y)
# a_p = log(a) --> e**(a_p) = a
# y_p = a_p + b*x

y_p = np.log(y)

coefs = np.polyfit(x, y_p, 1)

b = coefs[0]
a_p = coefs[1]
a = np.exp(a_p)

y_fit = a*np.exp(b*x)

plt.plot(x, y_fit)
plt.plot(x, y, "o")
plt.grid()
plt.show()