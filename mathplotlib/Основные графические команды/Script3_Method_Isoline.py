import matplotlib.pyplot as plt
import numpy as np




dat = np.random.random(200).reshape(20,10) # создаём матрицу значений



fig=plt.figure()
pc=plt.pcolor(dat)      #метод псевдографики pcolor
plt.colorbar(pc)
plt.title('Simple pcolor plot')

fig = plt.figure()
me = plt.imshow(dat)
plt.colorbar(me)
plt.title('Simple imshow plot')


plt.show()
