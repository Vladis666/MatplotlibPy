import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return np.sin(x) * np.exp(-np.exp(x / 10))


fig = plt.figure(figsize=(7, 4))
ax = fig.add_subplot()

x = np.arange(-10 * np.pi, 10 * np.pi, 0.1)
#ax.plot(x, f(x))
ax.loglog(x, f(x))
#ax.set_xscale('symlog', linthresh = 2)
ax.grid()

plt.show()
