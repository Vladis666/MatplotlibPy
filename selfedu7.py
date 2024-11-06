import numpy as np
import matplotlib.pyplot as plt

fig = plt.figure(facecolor="lightpink")
ax = fig.add_subplot()
ax.set_facecolor("lightyellow")

plt.figtext(0.05, 0.6, "little girls ")
fig.suptitle("Gentle pussy")
ax.set_xlabel("ox")
ax.set_xlabel("oy")
ax.text(0.05, 0.1, "Some text")
ax.annotate("Annotation", xy=(0.2, 0.4), xytext=(0.6, 0.7), arrowprops={"facecolor": "gray", "shrink": 0.1})

plt.show()
