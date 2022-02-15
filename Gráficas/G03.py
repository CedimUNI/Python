import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

r = np.linspace(0, 1.25, 500)
p = np.linspace(0, 2*np.pi, 500)
R, P = np.meshgrid(r, p)

x = lambda r,p: r*np.cos(p)
y = lambda r,p: r*np.sin(p)
z = lambda r,p: (r**2-1)**2

surf = ax.plot_surface(x(R,P), y(R,P), z(R,P), cmap=cm.plasma)

ax.set_zlim(0, 1)
ax.set_xlabel(r'$\phi_\mathrm{real}$')
ax.set_ylabel(r'$\phi_\mathrm{im}$')
ax.set_zlabel(r'$V(\phi)$')

fig.colorbar(surf, shrink=0.5, aspect=10)

plt.show()