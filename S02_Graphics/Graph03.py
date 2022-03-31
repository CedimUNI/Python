import numpy as np
import matplotlib.pyplot as plt

a = 2
theta = np.linspace(0, 2*np.pi, 100)
r = lambda theta: 2*a*np.sin(2*theta)

fig, ax = plt.subplots(subplot_kw = {'projection':'polar'})
ax.plot(theta, r(theta))
ax.set_rmax(4)
ax.set_rticks([0, 1, 2])
ax.set_rlabel_position(-22.5)

ax.set_title('1º Gráfica polar', va='bottom')

plt.show()