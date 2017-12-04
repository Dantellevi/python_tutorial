#Логарифмические координаты
"""

Команды semilogx, semilogy и loglog позаимствованы из
matlab’а и понимают такой же набор параметров, как и
plot:
"""


import numpy as np
import matplotlib.pyplot as plt


# plt.rc('text',usetex=True)
# plt.rc('font', family='serif')
x=np.logspace(-1,1,50)
plt.subplot(131)
plt.title('semologx')
plt.semilogx(x,x+1.0/x)
plt.subplot(132)
plt.title('semology')
plt.semilogy(x,x+1.0/x)
plt.subplot(133)
plt.loglog(x,x+1.0/x)
plt.title('loglog')

plt.show()
