import cv2
import numpy as np

img=cv2.imread('ImageTest.JPG')
roes,cols=img.shape[:2]
kernel_identity=np.array([[0,0,0],[0,1,0],[0,0,0]])     #матрица нулевой степени размытия
kernel3x3=np.ones((3,3),np.float32)/9.0                 #ядро размытия размером 3х3(только не четные числа)
kernel5x5=np.ones((5,5),np.float32)/25.0                #ядро размытия размером 5х5(только не четные числа)

cv2.imshow('Origin',img)

outImg=cv2.filter2D(img,-1,kernel_identity)             #Производим размытие изображения
cv2.imshow('Identity filter', outImg)


outImg3x3=cv2.filter2D(img,-1,kernel3x3)                #Производим размытие изображения
cv2.imshow('3x3 filter', outImg3x3)

outImg5x5=cv2.filter2D(img,-1,kernel5x5)                #Производим размытие изображения
cv2.imshow('5x5 filter', outImg5x5)

cv2.waitKey(0)




