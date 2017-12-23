import numpy as np
import cv2

img=cv2.imread('ImageTest.JPG')
cv2.imshow('Origin',img)


size=15


#генерируем ядра для размытия
kernel_motion_blur=np.zeros((size,size))
kernel_motion_blur[int((size-1)/2),:]=np.ones(size)

kernel_motion_blur=kernel_motion_blur/size


#Применяем ядра размытия на входное изображение
output=cv2.filter2D(img,-1,kernel_motion_blur)

cv2.imshow('Motion Blur',output)
cv2.waitKey(0)




