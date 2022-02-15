import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(projection='3d')

t = np.linspace(-5, 5, 100)

x = lambda t: t
y = lambda t: t**2
z = lambda t: t**3

ax.plot(x(t),y(t),z(t))

plt.show()