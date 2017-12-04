
"""
Команда plot_wireframe имеет два необязательных
аргумента cstride и rstride, задающие шаг сетки по рядам
и колонкам. Иногда они позволяют улучшить вид
графика.
Толщину и цвет линии можно задавать через аргументы
lw и color.
Начальный угол зрения задается дополнительной
командой view_init(<угол места>,<азимут>).
Обратите также внимание, что подписи по осям
задаются несколько иначе, чем в двумерных графиках.
"""

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


ax=axes3d.Axes3D(plt.gcf())     #создание объекта 3D плотера(Получите ссылку на текущую цифру)
N=31
x=np.linspace(0,N-1,N)
y=np.linspace(0,N-1,N)
X,Y=np.meshgrid(x,y)       #Обратные координатные матрицы из векторов координат.
Z=np.fromfunction(lambda y,x:np.sin((0.2*(x-N/2)))*(y-N/2),(N,N))   #Постройте массив, выполнив функцию над каждой координатой
ax.view_init(50,-60)    #Начальный угол зрения
ax.plot_wireframe(X,Y,Z,color='#FF8000',lw='2',cstride=7,rstride=1)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x,y)')
plt.show()



