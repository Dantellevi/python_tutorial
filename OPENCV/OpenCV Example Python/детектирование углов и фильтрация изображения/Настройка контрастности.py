import numpy as np
import cv2

img=cv2.imread('Contrast.JPG',0)

histeq=cv2.equalizeHist(img)    #Уравнивает гистограмму полутонового изображения

cv2.imshow('Input',img)
cv2.imshow('Histogram equlized', histeq)

cv2.waitKey()



