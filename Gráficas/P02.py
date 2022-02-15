import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

u = np.linspace(0,2*np.pi,100)
v = np.linspace(-1,1,100)

U, V = np.meshgrid(u,v)

x = lambda u,v: (1-v*np.sin(u/2))*np.cos(u)
y = lambda u,v: (1-v*np.sin(u/2))*np.sin(u)
z = lambda u,v: v*np.cos(u/2)

ax.plot_surface(x(U,V), y(U,V), z(U,V))

plt.show()