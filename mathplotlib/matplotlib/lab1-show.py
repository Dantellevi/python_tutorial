# Постройка простого графика без настроек
import matplotlib.pyplot as plt
import math
import numpy as np
x=np.linspace(-10,10,50)    # набор данных
y=np.sin(x)/x #выходной параметр

plt.plot(x,y)
plt.savefig('plot2.pdf')
plt.show()

