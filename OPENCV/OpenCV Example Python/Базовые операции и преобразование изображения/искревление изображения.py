import cv2
import numpy as np
import math


img=cv2.imread('ImageTest.JPG',cv2.IMREAD_GRAYSCALE)
rows,cols=img.shape


#===================Вертикальное искревление=======================

img_out=np.zeros(img.shape,dtype=img.dtype) #создаем пустую матрицу
for i in range(rows):
    for j in range(cols):
        offset_x=int(25.0*math.sin(2*3.14*i/180)) #задаем смещение
        offset_y=0                                #задаем смещение
        if j+offset_x<rows:
            img_out[i,j]=img[i,(j+offset_x)%cols]   #зададим значение пикселя
        else:
            img_out[i,j]=0


cv2.imshow('Input',img)
cv2.imshow('Vertical wave',img_out)


#==============================Горизонтальное искремление==============

img_out=np.zeros(img.shape,dtype=img.dtype)

for i in range(rows):
    for j in range(cols):
        offset_x=0
        offset_y=int(16.0*math.sin(2*3.14*j/150))
        if i+offset_y<rows:
            img_out[i,j]=img[(i+offset_y)%rows,j]
        else:
            img_out[i,j]=0


cv2.imshow('Horizontal wave',img_out)

#========================совмещенное горизонтальное и вертикальное искревление========
img_out=np.zeros(img.shape,dtype=img.dtype)

for i in range(rows):
    for j in range(cols):
        offset_x=int(20.0*math.sin(2*3.14*i/150))
        offset_y = int(20.0 * math.cos(2 * 3.14 * i / 150))
        if i+offset_y<rows  and j+offset_x<cols:
            img_out[i,j]=img[(i+offset_y)%rows,(j+offset_x)%cols]
        else:
            img_out[i,j]=0

cv2.imshow('Multidirection wave',img_out)


#=====================Вогнутый эффект======================

img_out=np.zeros(img.shape,dtype=img.dtype)
for i in range(rows):
    for j in range(cols):
        offset_x=int(128.0*math.sin(2*3.14*i/(2*cols)))
        offset_y=0
        if j+offset_x<cols:
            img_out[i,j]=img[i,(j+offset_x)%cols]
        else:
            img_out[i,j]=0

cv2.imshow('Concave',img_out)
cv2.waitKey()




