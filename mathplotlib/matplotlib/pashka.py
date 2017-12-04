import numpy as np

import matplotlib.pyplot as plt

x=np.arange(0,16)
y=5*np.sqrt(x)+((np.sqrt(x)-2)**2)-(x+4)
plt.plot(x,y,c='#7F007F',lw=3,marker='o',mec='#FF0000',mfc='#FFFF00',mew=2,ms=5)
plt.title('График функции')
plt.grid()
i=1
j=1
for xi in x:
    print('x'+str(i)+'='+str(xi))
    i+=1

for yi in y:
    print('y'+str(j)+'='+str(yi))
    j+=1
plt.show()
