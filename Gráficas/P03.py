import numpy as np
import matplotlib.pyplot as plt

ax = plt.figure().add_subplot(projection='3d')

t = np.linspace(-2,2,100)
x = lambda t: t
y = lambda t: t**2
z = lambda t: t**3

ax.plot(x(t), y(t), z(t))

ax.set_xticks(np.linspace(-2,2,5))
ax.set_yticks(np.linspace(np.min(y(t)),np.max(y(t)),5))
ax.set_zticks(np.linspace(np.min(z(t)),np.max(z(t)),6))

plt.show()