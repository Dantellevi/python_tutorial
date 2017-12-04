#Ошибки измерения

"""
Команда errorbar(x,y,xerr=<данные>,yerr=<данные>)
рисует график с указанием ошибок измерения.
Параметры xerr, yerr могут быть массивами такой же
длины, как x, y, скалярами либо отсутствовать.
Остальные необязательные параметры такие же, как у
команды plot:

"""

import matplotlib.pyplot as plt
import numpy as np

x=np.linspace(-10,10,20)
y=np.sin(x)/x+0.2*np.random.rand(20)-0.1
dx=0.5
dy = 0.1+abs(x)/100
plt.errorbar(x, y, xerr=dx, yerr=dy, c='blue', ls='--',\
lw=2, marker='o', mfc='white', ms=5)
plt.xlim(-12,12)
plt.grid()
plt.show()
