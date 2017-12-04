#Масштаб по осям


import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,50)
y=np.sin(x)/x
plt.plot(x,y,'mD--')
plt.xlim(1,5)   #установка значений
plt.ylim(0,1.1)
plt.show()

