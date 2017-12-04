
#Легенда
"""
Команда legend создает описания к графикам. Ее
второй (необязательный) аргумент может быть цифрой
от 0 до 9, кодирующей расположение легенды как в
matlab’е.
"""

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-10,10,50)
plt.plot(x,np.sin(x)/x)
plt.plot(x,1-x**2/6+x**4/120)
plt.ylim(-0.3,1.1)
plt.legend(('f(x)','Taylor','Taylor 5'),shadow=True, fancybox=True)
plt.show()
