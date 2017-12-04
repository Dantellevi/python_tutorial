#Независимые переменные

"""

В качестве независимых переменных x, y использовались
индексы массива. Можно задать их и явно:

"""

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-np.pi,np.pi,50)
y=np.linspace(-1,1,50)
z=np.matrix(y).T*np.sin(x)
plt.contour(x,y,z,np.linspace(-1,1,21))
plt.xlabel('x')
plt.ylabel('y')
plt.show()

