import matplotlib.pyplot as plt
import numpy as np

x = np.arange(-2*np.pi, 2*np.pi, 0.1)
u = np.sin(x)*np.cos(x)
v = np.cos(x)
uu, vv = np.meshgrid(u,v)   #Обратные координатные матрицы из векторов координат.


N = 100
x1 = np.random.random(N).reshape((10, 10))
y1 = np.random.random(N).reshape((10, 10))


# streamplot()
fig = plt.figure()
plt.streamplot(x, x, uu, vv)
plt.title('Simple stream plot')
plt.grid(True)

# quiver()
fig = plt.figure()
plt.quiver(x1, y1, color='green')
plt.title('Simple quiver plot')
plt.grid(True)

plt.show()



