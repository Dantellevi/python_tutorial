#Контурный график

"""
Команда contour(z,levels) рисует контурный график
двумерного массива z. Параметр levels – одномерный
массив, задающий изоуровни:

"""

import numpy as np
import matplotlib.pyplot as plt


x=np.linspace(-np.pi,np.pi,50)
y=np.linspace(-1,1,50)
z=np.matrix(y).T*np.sin(x)
plt.contour(z,np.linspace(-1,1,21))
plt.show()
