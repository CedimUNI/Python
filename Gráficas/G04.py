import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

fig = plt.figure(figsize=(10,4))

# Primer subploteo
ax = fig.add_subplot(1, 2, 1, projection='3d')

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)
z = lambda x, y: np.sin(np.sqrt(x**2+y**2))

surf = ax.plot_surface(X, Y, z(X,Y), cmap=cm.coolwarm)
ax.set_zlim(-1.01, 1.01)
fig.colorbar(surf, shrink=0.5, aspect=10)

# Segundo Subploteo
ax = fig.add_subplot(122, projection='polar', aspect=0.5)

a = 2
theta = np.linspace(0, 2*np.pi, 100)
r = lambda theta: a**2*np.sin(2*theta)

ax.plot(theta, r(theta))
ax.set_rmax(4)
ax.set_rticks(np.linspace(0,4,2))
ax.set_rlabel_position(-22.5)

fig.tight_layout()

plt.show()