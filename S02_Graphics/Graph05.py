import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

z = lambda x, y: np.sin(np.sqrt(x**2+y**2))

surf = ax.plot_surface(X, Y, z(X, Y), cmap = cm.inferno)

ax.set_zlim(-1.5, 1.5)
fig.colorbar(surf, shrink = 0.5, aspect = 10)
plt.show()