from pylab import *
import matplotlib.pyplot as plt
import numpy as np

#X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
#C, S = np.cos(X), np.sin(X)

#plt.plot(X, C)
#plt.plot(X, S)

#plt.show()

#x = linspace(0, 5, 10)
#y = x**2
#figure()
#plot(x, y, 'r')
#xlabel('dias')
#ylabel('horas')
#title('aumento de errores de capa 8')
#show()

n = 256
X = np.linspace(-np.pi, np.pi, n, endpoint=True)
Y = np.sin(2 * X)

plt.axes([0.025, 0.025, 0.95, 0.95])

plt.plot(X, Y + 1, color='black', alpha=1.00)
plt.fill_between(X, 1, Y + 1, color='black', alpha=.25)

plt.plot(X, Y - 1, color='black', alpha=1.00)
plt.fill_between(X, -1, Y - 1, (Y - 1) > -1, color='black', alpha=.25)
plt.fill_between(X, -1, Y - 1, (Y - 1) < -1, color='red',  alpha=.25)

plt.xlim(-np.pi, np.pi)
plt.xticks(())
plt.ylim(-2.5, 2.5)
plt.yticks(())

plt.show()