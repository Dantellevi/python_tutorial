import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-np.pi,np.pi,50)
y=np.linspace(-1,1,50)
z=np.matrix(y).T*np.sin(x)
cf=plt.contourf(x,y,z,np.linspace(-1,1,21))
plt.colorbar(cf)
plt.xlabel('x')
plt.ylabel('y')
plt.show()