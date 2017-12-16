import cv2
import numpy as np
img=cv2.imread('bookpage.jpg')
#переводит пиксель в черно-белое если больше порога срабатывания
retval,threhold=cv2.threshold(img,12,255,cv2.THRESH_BINARY)

#в серых оттенках
grayscaled=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#дополнителный фильт для серых оттенков
retval2,threhold2=cv2.threshold(grayscaled,12,255,cv2.THRESH_BINARY)
#Гаусовский фильтр
gaus=cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

retval3,threhold3=cv2.threshold(grayscaled,125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow('gauseFilter',gaus)
cv2.imshow('gray-Termo',threhold2)
cv2.imshow('image',img)
cv2.imshow('gray',grayscaled)
cv2.imshow('image',img)
cv2.imshow('Mono', threhold)
cv2.imshow('Bin+OTSU', threhold3)
cv2.waitKey(0)
cv2.destroyAllWindows()
