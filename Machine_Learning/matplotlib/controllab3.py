import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(-12,120,200)

plt.plot(x,(np.sin(x)/np.cos(x))/x)

plt.plot(x,(np.cos(x)/np.sin(x))/x)

plt.show()
