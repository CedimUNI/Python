import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import ticker
from matplotlib.ticker import LinearLocator
import numpy as np

fig, ax = plt.subplots(subplot_kw={'projection':'3d'})

x = np.linspace(-5,5,100)
y = np.linspace(-5,5,100)

X, Y = np.meshgrid(x, y)

z = lambda x,y: np.sin(np.sqrt(x**2+y**2))

surf = ax.plot_surface(X, Y, z(X,Y), cmap=cm.viridis)

ax.set_zlim(-1.01, 1.01)

ax.zaxis.set_major_locator(LinearLocator(5))

ax.zaxis.set_major_formatter(ticker.StrMethodFormatter('{x:.3f}'))

fig.colorbar(surf, shrink = 0.5, aspect = 10)

plt.show()