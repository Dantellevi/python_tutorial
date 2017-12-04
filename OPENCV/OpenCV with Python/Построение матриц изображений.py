import cv2
import numpy as np

import os

#Получаем массив 120000 элементов
randomByteArray=bytearray(os.urandom(120000))


flatNumpyArray=np.array(randomByteArray)

#конвертируем массив в матрицу 400х300 в оттенках серого
grayImage=flatNumpyArray.reshape(300,400)

#Конвертируем массив в 400х100 в цвете
colorImage=flatNumpyArray.reshape(100,400,3)
cv2.imshow('400x300 gray',grayImage)
cv2.imshow('400x100 color',colorImage)
cv2.waitKey()
cv2.destroyAllWindows()
