"""
2D-сверление (фильтрация изображений)

Как и в одномерных сигналах,
 изображения также могут фильтроваться
 различными фильтрами нижних частот (LPF),
 фильтрами высоких частот (HPF) и т. Д.
 LPF помогает удалять шумы, размытие изображений и т. Д.
 Фильтры HPF помогают находить края в изображений.

OpenCV предоставляет функцию cv2.filter2D ()
для свертки ядра с изображением.

"""



import cv2
import numpy as np
from matplotlib import pyplot as plt


img=cv2.imread('originImg.JPG') #считываем изображения

kernel=np.ones((5,5),np.float32)/25 #строим ядро матрицы
dst=cv2.filter2D(img,-1,kernel)     #производим фильтрацию

#================Вывод результатов=======================
plt.subplot(121),plt.imshow(img),plt.title('Origin')
plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(dst),plt.title('Averaging')
plt.xticks([]), plt.yticks([])
plt.show()
#========================================================

