import numpy as np
import matplotlib.pyplot as plt

x = lambda t: t**2-4
y = lambda t: t/2
t = np.linspace(-10, 10, 100)

plt.plot(x(t), y(t))
plt.show()