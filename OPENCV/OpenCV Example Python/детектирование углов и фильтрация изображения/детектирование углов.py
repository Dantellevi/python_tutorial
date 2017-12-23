import cv2
import numpy as np

img=cv2.imread('adge.JPG',cv2.IMREAD_GRAYSCALE)
rows,colms=img.shape

sobel_horizontal=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)  #преобразование собеля для детектирования горризонтальных углов
sobel_vertical=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)    #преобразование собеля для детектирования вертикальных углов
laplacian=cv2.Laplacian(img,cv2.CV_64F) # Метод обнаружение углов Лапласса
canny=cv2.Canny(img,50,240)



cv2.imshow('Origin',img)
cv2.imshow('sobel horizontal',sobel_horizontal)
cv2.imshow('sobel_vertical',sobel_vertical)
cv2.imshow('laplas convection',laplacian)
cv2.imshow('Canny convection',canny)


cv2.waitKey()
