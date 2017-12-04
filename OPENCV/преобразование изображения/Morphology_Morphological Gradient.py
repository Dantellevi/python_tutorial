"""

Это разница между расширением
 и эрозией изображения.

"""

import numpy as np
import cv2

img = cv2.imread('MorfoImage.JPG')  # считываем изображение
kernel = np.ones((5, 5), np.uint8)  # ядро свертки

gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)  # операция градиента

cv2.imshow('origin',img)        #отображение
cv2.imshow('gradient Image',gradient)  #отображение

cv2.waitKey()
cv2.destroyAllWindows()