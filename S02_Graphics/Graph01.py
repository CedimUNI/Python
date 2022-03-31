import numpy as np
import matplotlib.pyplot as plt

f = lambda x: np.sin(x)
x = np.linspace(0, 2*np.pi, 100)
y = f(x)

plt.plot(x, y)
plt.show()