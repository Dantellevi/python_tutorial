# Легенда

"""

Расположение легенды можно также явно задать парой
числе от 0 до 1 (в этом случае необходимо явно указать
ключевое слово loc):

"""

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-10,10,50)
plt.plot(x,np.sin(x)/x,ls=':')
plt.plot(x,1-x**2/6,ls='-')
plt.plot(x,1-x**2/6+x**4/120,ls='--')
plt.ylim(-0.3,1.1)
plt.legend(('f(x)','Taylor','Taylor 5'),shadow=True, fancybox=True,loc=(0.8,0.4))
plt.show()
