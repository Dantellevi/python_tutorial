# Сетка

"""
Как и при рисовании самого графика, можно указывать
цвет и вид линий сетки:

"""
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-10,10,50)
plt.plot(x,np.sin(x)/x)
plt.plot(x,1-x**2/6)
plt.plot(x,1-x**2/6+x**4/120)
plt.ylim(-0.3,1.1)
plt.legend(('f(x)','Teylor 3','Taylor 5'),shadow=True, fancybox=True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.text(-9.0,0.16,'Maximum')
#цвет|тип сетки|толщина
plt.grid(c='#BFEFEF',ls='-', lw=0.5)
plt.show()