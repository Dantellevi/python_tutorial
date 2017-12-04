import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d


ax=axes3d.Axes3D(plt.gcf())     #создание объекта 3D плотера(Получите ссылку на текущую цифру)
N=31
x=np.linspace(0,N-1,N)
y=np.linspace(0,N-1,N)
X,Y=np.meshgrid(x,y)       #Обратные координатные матрицы из векторов координат.
Z=np.fromfunction(lambda y,x:np.sin((0.2*(x-N/2)))*(y-N/2),(N,N))   #Постройте массив, выполнив функцию над каждой координатой
ax.plot_wireframe(X,Y,Z)
plt.show()



