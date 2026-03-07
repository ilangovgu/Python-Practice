import numpy as np

import matplotlib.pyplot as plt

scores = np.random.normal(loc=80, scale=10, size=100)

plt.hist(scores, bins=10,
         color="grey",
         edgecolor="black")
plt.title("Histogram")
plt.xlabel("X label")
plt.ylabel("# Y label")

plt.show()