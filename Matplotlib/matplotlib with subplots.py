import numpy as np

import matplotlib.pyplot as plt

figure, axes = plt.subplots(2, 2)

x = np.array([1, 2, 3, 4, 5])

axes[0, 0].plot(x, x*2, color="red")
axes[0, 0].set_title("Plot A")

axes[0, 1].plot(x, x**2, color="green")
axes[0, 1].set_title("Plot B")

axes[1, 0].plot(x, x**3, color="orange")
axes[1, 0].set_title("Plot C")

axes[1, 1].plot(x, x**4, color="grey")
axes[1, 1].set_title("Plot D")

plt.tight_layout()
plt.show()