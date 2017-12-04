#Несколько кривых на одном графике

#Каждая команда plot добавляет свою кривую:

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,60)
plt.plot(x,np.sin(x)/x)
plt.plot(x,1-x**2/6)
plt.plot(x,1-x**2/6+x**4/120)
plt.ylim(-0.3,1.1)
plt.show()
