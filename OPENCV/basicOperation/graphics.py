import matplotlib.pyplot as plt
import numpy as np


t=np.arange(0,10,1)
A=100
B=2
X=A+B*t
plt.plot(t,X,c='#7F007F',lw=3,marker='o',mec='#FF0000',mfc='#FFFF00',mew=2,ms=5)
plt.grid()
plt.title('График функции')
i=1
j=1
# for xi in t:
#     print('x'+str(i)+'='+str(xi))
#     i+=1
#
# for yi in X:
#     print('y'+str(j)+'='+str(yi))
#     j+=1
plt.show()
