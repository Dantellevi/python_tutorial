#	Определение	контура	при	помощи	функции	Canny
import cv2
import numpy as np

lowThresh=100
HighTresh=200

img=cv2.imread('Cannyimg.JPG')
edges=cv2.Canny(img,lowThresh,HighTresh)
cv2.imshow('Averaging',img)             #отображение
cv2.imshow('GausianBlur', edges)         #отображение

cv2.waitKey(0)                          #ожидание нажатия клавиши
cv2.destroyAllWindows()   