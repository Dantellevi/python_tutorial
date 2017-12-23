import numpy as np
import cv2



img=cv2.imread('ImageTest.JPG')
cv2.imshow('Origin',img)

#генерируем ядра для преобразования

kernel_sharpen_1=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
kernel_sharpen_2=np.array([[-1,-1,-1],[-1,7,-1],[-1,-1,-1]])

kernel_sharpen_3=np.array([[-1,-1,-1,-1,-1],
                           [-1,2,2,2,1],
                           [-1,2,8,2,1],
                           [-1,2,2,2,1],
                           [-1,-1,-1,-1,-1]])/8.0

#применем дифференциальные ядра на входную матрицу
output1=cv2.filter2D(img,-1,kernel_sharpen_1)
output2=cv2.filter2D(img,-1,kernel_sharpen_2)
output3=cv2.filter2D(img,-1,kernel_sharpen_3)

cv2.imshow('SHarpening',output1)
cv2.imshow('Excessive SHarpening',output2)
cv2.imshow('Edge Enhancement',output3)
cv2.waitKey(0)

