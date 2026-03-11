# Matplotlib Subplots

import matplotlib.pyplot as plt
import numpy as np

figure, axes=plt.subplots(2,2)          # Axes is a numpy library

x=np.array([1,2,3,4,5])                 # Giving data for x

axes[0,0].plot(x,x*2,color=("red"))     # For the plot (0,0) as continues below
axes[0,0].set_title("Plot A")


axes[0,1].plot(x,x**2,color=("green"))
axes[0,1].set_title("Plot B")


axes[1,0].plot(x,x**3,color=("orange"))
axes[1,0].set_title("Plot C")


axes[1,1].plot(x,x**4,color=("grey"))
axes[1,1].set_title("Plot A")




plt.tight_layout()                      # Giving space to the plots
plt.show()
