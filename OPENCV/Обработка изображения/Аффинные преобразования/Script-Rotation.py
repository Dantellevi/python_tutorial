import cv2
import numpy as np

img=cv2.imread('Image.JPG',0)
rows,cols=img.shape

M = cv2.getRotationMatrix2D((cols/2,rows/2),45,1)   #задаем поворот изображение(последний параметр zoom)
dst = cv2.warpAffine(img,M,(cols,rows))             # производим преобразование

cv2.imshow('origin',img)
cv2.imshow('Affine transform-Rotation',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()