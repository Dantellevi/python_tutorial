import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(-10,10,50)
plt.plot(x,np.sin(x)/x)
plt.plot(x,1-x**2/6)
plt.ylim(-0.3,1.1)
plt.title('Taylor expantion')
sp=plt.axes([0.62,0.6,0.25,0.19],axisbg='#BFFFFF')
plt.plot(x,x**2/6+x**4/120)
plt.title('Taylor 5')
plt.show()
