import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import ticker
from matplotlib.ticker import LinearLocator
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

n = 50

# Creamos las mallas a utilizar
r = np.linspace(0, 1.25, n)
p = np.linspace(0, 2*np.pi, n)
R, P = np.meshgrid(r, p)

# Computamos las funciones
x = lambda r,p: r*np.cos(p)
y = lambda r,p: r*np.sin(p)
z = lambda r,p: (r**2-1)**2

# Graficamos la superficie
surf = ax.plot_surface(x(R,P), y(R,P), z(R,P), cmap=cm.plasma)

# Agregamos límites y ponemos etiquetas en LaTex.
ax.set_zlim(0, 1)
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')

ax.zaxis.set_major_locator(LinearLocator(5)) 

fig.colorbar(surf, shrink=0.5, aspect=10)

plt.show()