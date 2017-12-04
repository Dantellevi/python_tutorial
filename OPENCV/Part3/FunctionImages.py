import numpy as np

import cv2
lenaimg=cv2.imread('ImageTest.JPG')
#cv2.imwrite('LenaCopy.jpg',lenaimg)
cv2.imshow('Hello, Lena!',lenaimg)
#=============================================
lena_color=cv2.imread('LenaCopy.jpg',cv2.IMREAD_COLOR)
lena_unchanged=cv2.imread('LenaCopy.jpg',cv2.IMREAD_UNCHANGED)
lena_grayscale=cv2.imread('LenaCopy.jpg',cv2.IMREAD_GRAYSCALE)

print(type(lena_color))
print('RGB shape:',lena_color.shape)    #RGB shape:(512,512,3)
print('ARGB shape:',lena_unchanged.shape)    #ARGB shape:(512,512,3)
print('Gray shape:',lena_grayscale.shape)    #Gray shape:(512,512,3)
print('lena.dtype:',lena_color.dtype)    #uint8
print('Gray shape:',lena_color.size)    #size 786432

#======================xПример работы с областями=======================
ln=lenaimg.copy()
n_rows,n_cols,n_channels=ln.shape
lena_top=ln[0:(int)(n_rows/2),:]
lena_left=ln[:,0:(int)(n_cols/2)]
lena_top[:]=lena_top[::-1]  #меняем местами первый становится последним и наоборот
lena_left[:]=lena_left[::-1]

cv2.imshow('Lena Broken',ln)

#============================Арифметические операции над изображением=================================

# lena_gray=cv2.imread('LenaCopy.jpg',cv2.IMREAD_GRAYSCALE)
# nn_rows,nn_cols=lena_gray.shape
# lena_left_half=lena_gray[:,0:(int)(nn_cols/2)]
# lena_right_half=lena_gray[:,(int)(nn_cols)/2:nn_cols]
#
# lena_left_half=cv2.subtract(lena_left_half,256)
# lena_right_half=lena_right_half-256
#
# lena_gray[:,(int)(nn_cols/2)]=lena_left_half
# lena_gray[:,nn_cols/2:nn_cols]=lena_right_half
#
# cv2.imshow('Lena Overflow',lena_gray)

#=========================Доступ к каналу==================================
imgL=cv2.imread('LenaCopy.jpg')
b,g,r=cv2.split(imgL)
#r=100
print(b)
print('--------------------')
print(g)
print('--------------------')
print(r)
print('--------------------')
rn=r.copy()
rn[20:80,:]=255
#rgb=cv2.merge((r,g,b))
rgb=cv2.merge((b,g,rn))
#rgb[:,:,1]=0
cv2.imshow('Lena_R_G_B',rgb)
cv2.waitKey(0)



#================================изменение цветового пространства==============================

leni=cv2.imread('LenaCopy.jpg')

leni=cv2.cvtColor(leni,cv2.COLOR_BGR2GRAY)
leni=cv2.cvtColor(leni,cv2.COLOR_GRAY2BGR)
cv2.imshow('Lena Gray', leni)



#===============================================================
cv2.waitKey(0)
cv2.destroyAllWindows()