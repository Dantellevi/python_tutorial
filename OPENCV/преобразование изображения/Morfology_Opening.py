"""
Открытие - это еще одно название эрозии, за которым следует расширение .
Это полезно для устранения шума, как мы объясняли выше.
Здесь мы используем функцию cv2.morphologyEx ()


"""

import numpy as np
import cv2

img = cv2.imread('shume.JPG')  # считываем изображение
kernel = np.ones((5, 5), np.uint8)  # ядро свертки
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)  # операция открытие (очистка от шумов)

cv2.imshow('origin',img)        #отображение
cv2.imshow('Opening Image',opening)  #отображение


cv2.waitKey()
cv2.destroyAllWindows()

