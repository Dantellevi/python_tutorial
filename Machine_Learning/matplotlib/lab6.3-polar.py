#Полярные координаты

"""
Команда polar(theta,r) рисует график в полярных
координатах. Остальные необязательные параметры
такие же, как у команды plot:

"""

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-2*np.pi,2*np.pi,100)
y=np.sin(x)/x
plt.polar(x,y,c='blue',lw=2)
#plt.grid()
plt.show()