import cv2
import numpy as np

img_emboss_unput=cv2.imread('ImageTest.JPG')

#генерируем ядра дря конвертации
kernel_emboss_1=np.array([[0,-1,-1],
                          [1,0,-1],
                          [1,1,0]])


kernel_emboss_2=np.array([[-1,-1,0],
                          [-1,0,1],
                          [0,1,1]])

kernel_emboss_3=np.array([[1,0,0],
                          [0,0,0],
                          [0,0,-1]])


#конвертируем в оттенки серого

gray_img=cv2.cvtColor(img_emboss_unput,cv2.COLOR_BGR2GRAY)

#приминяем ядра для конвертации

out1=cv2.filter2D(gray_img,-1,kernel_emboss_1)+128
out2=cv2.filter2D(gray_img,-1,kernel_emboss_2)+128
out3=cv2.filter2D(gray_img,-1,kernel_emboss_3)+128



cv2.imshow('Origin',img_emboss_unput)
cv2.imshow('Embrossing - South West',out1)
cv2.imshow('Embrossing - South East',out2)
cv2.imshow('Embrossing - North West',out3)
cv2.waitKey()

