# Несколько картинок в одном скрипте
"""
Как правило, все графики к данной статье или другому
документу удобно генерировать одним скриптом. При
этом для перехода от одного графика к другому
используется команда figure():

"""

import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,50)
plt.plot(x,np.sin(x)/x)
plt.plot(x,1-x**2/6)
plt.ylim(-0.3,1.1)
plt.figure()
plt.plot(x,1-x**2/6+x**4/120)
plt.show()
