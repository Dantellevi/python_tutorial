#Фильтр затемнения(затемняет фон изображения)
import cv2
import numpy as np

img=cv2.imread('ImageTest.JPG')
rows,cols=img.shape[:2]

#генерирует маску для фильтк используя Гауссовское ядро

kernel_x=cv2.getGaussianKernel(cols,200)    #генерируем ядро гаусса по х
kernel_y=cv2.getGaussianKernel(rows,200)    #генерируем ядро гаусса по у

kernel=kernel_y*kernel_x.T      #перемножаем два ядра

mask=255*kernel/np.linalg.norm(kernel)  #создаем маску Vignette
output=np.copy(img) #копируем входное изображения в выходное

#Применение маски к каналам изображения
for i in range(3):
    output[:,:,1]=output[:,:,i]*mask    #перемножаем значения пикселей на значение маски

cv2.imshow('Original',img)
cv2.imshow('Vignette',output)
cv2.waitKey()




