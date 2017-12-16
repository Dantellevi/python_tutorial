import matplotlib.pyplot as plt
import numpy as np

fig=plt.figure()        #создаем полотно
ax=fig.add_subplot(111)

N=10                    #переменная для набора данных
x=np.arange(1,N+1,1)    #генерируем набор данных
y=20.*np.random.randn(N)
rgb=np.array([204,255,51])/255  #окраска RGB
myhex='#660099'                  #окраска hex
ax.plot(x,y,color=myhex)        #выводим на полотно
ax.bar(x,y,color=rgb,alpha=0.75,align='center')
ax.set_xticks(x)   # установка делений на оси OX
ax.set_xlim(np.min(x)-1, np.max(x)+1)   # ограничение области изменения по оси OX
ax.grid(True)
plt.show()