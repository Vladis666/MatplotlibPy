import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.ticker import NullFormatter, FormatStrFormatter, FuncFormatter, ScalarFormatter, FixedFormatter

def x_ax_formation(x, pos):
    return f"[{x}]" if x<0 else f"({x})"

def y_ax_formation(x, pos):
    return f"[{x}]" if x<0 else f"({x})"

fig = plt.figure(figsize=(7,4))
ax = fig.add_subplot()

matplotlib.rcParams["axes.formatter.limits"] = (-4,4)
sf = ScalarFormatter()
sf.set_powerlimits((-6,6))
ax.xaxis.set_major_formatter(FixedFormatter(['a','b','c','d','e','f','g','e']))
#ax.yaxis.set_major_formatter(ScalarFormatter(sf))

x = np.arange(-np.pi/2, np.pi, 0.05)

ax.plot(x, np.sin(x) * 1e10)

ax.grid()
plt.show()