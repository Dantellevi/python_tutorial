#Несколько графиков в одной картинке

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(0,12,50)
plt.subplot(221)    #метод ответственый за расположение графиков
plt.plot(x,np.sin((x)))
plt.subplot(222)
plt.plot(x,np.cos(x))
plt.subplot(223)
plt.plot(x,np.sin(x)**2)
plt.subplot(224)
plt.plot(x,np.cos(x)**2)
plt.show()
