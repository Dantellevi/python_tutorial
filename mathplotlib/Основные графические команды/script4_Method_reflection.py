import matplotlib.pyplot as plt
import numpy as np

dat = np.random.random(200).reshape(20,10) # создаём матрицу значений

fig=plt.figure()
cr=plt.contour(dat) #построение области значений
plt.colorbar(cr)    #построение линейки значений


plt.title('Simple contour plot')

fig = plt.figure()
cf = plt.contourf(dat)      #построение области значений
plt.colorbar(cf)            #построение линейки значений
plt.title('Simple contourf plot')

fig = plt.figure()
cf = plt.matshow(dat)
plt.colorbar(cf, shrink=0.7)
plt.title('Simple matshow plot')


plt.show()

