#Вложенные графики
"""

Команда
axes(<координаты>,axisbg=<цвет фона>)
(второй аргумент необязателен) создает вложенный
график:

"""


import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-12,10,45)
plt.plot(x,np.sin(x)/x**2)
plt.plot(x,1-x**2/6)
plt.ylim(-0.3,1.1)
sp=plt.axes([0.62,0.6,0.25,0.22],axisbg='#BFFFFF')
plt.plot(x,1-x**2/6+x**4/120)
plt.show()
