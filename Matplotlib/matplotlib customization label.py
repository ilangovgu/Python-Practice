import numpy as np

# Matplotlib & Numpy
# Customization

import matplotlib.pyplot as plt

a = np.array([1, 2, 3, 4, 5])
b = np.array([10, 20, 30, 40, 50])
c = np.array([100, 200, 300, 400, 500])
d = np.array([15, 4, 5, 6, 56])

line_style = dict(marker=".",
                  markersize=20,
                  markerfacecolor="#eb4034",
                  markeredgecolor="#eb4678",
                  linestyle="dashed",
                  linewidth=3,
                  color="#eb4034")

plt.grid(axis="x", linestyle="dotted",
         linewidth=2,
         color="blue")

plt.title("Graph", fontsize=25,
          family="calibri",
          fontweight="bold",
          color="#287aed")

plt.xlabel("Label 1", fontsize=25,
           family="calibri",
           fontweight="bold",
           color="#287aed")

plt.ylabel("Label 2", fontsize=25,
           family="calibri",
           fontweight="bold",
           color="#287aed")

plt.plot(a, b, **line_style)
plt.plot(a, c, **line_style)
plt.plot(a, d, **line_style)

plt.show()