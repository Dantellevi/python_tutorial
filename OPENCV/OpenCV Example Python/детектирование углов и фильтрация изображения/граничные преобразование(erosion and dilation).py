#========================Эрозия и расширения===================

import cv2
import numpy as np

img=cv2.imread('Morpgology.JPG',0)      #считываем в серых оттенках

kernel=np.ones((5,5),np.uint8)

img_erosion=cv2.erode(img,kernel,iterations=1)
img_dilation=cv2.dilate(img,kernel,iterations=1)

cv2.imshow('Input',img)
cv2.imshow('Errosion',img_erosion)
cv2.imshow('Dilation',img_dilation)

cv2.waitKey()




