"""
Только	что	описанный	метод	поиска	краев	в	1986	году	был	улучшен	J.	Canny	и
именуется	как	детектор	границ	Canny.	Отличие	алгоритма	Canny	от	более	простого
алгоритма,	основанного	на	преобразованиях	Лапласа,	в	том,	что	в	алгоритме	Canny
первые	производные	вычисляются	по	осям	x	и	y,	а	затем	объединяются	в	четырех
направлениях	производных.	Точки,	в	которых	эти	производные	достигают	локального
максимума	затем	рассматриваются	в	качестве	кандидатов	на	группировку	в	край.


"""


import cv2

import numpy as np

from matplotlib import pyplot as plt

img=cv2.imread('Canny.JPG',0)
res=cv2.resize(img,None,fx=2,fy=2,interpolation=cv2.INTER_AREA)
edges=cv2.Canny(res,10,50)      #распознавание краев(параметры:img-входное изображение,10-первый порог для процедуры гистерезиса,50-второй порог для процедуры гистерезиса.)
edges2=cv2.Canny(res,100,150)

plt.subplot(2,2,1),plt.imshow(res,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,2),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image 10x50'), plt.xticks([]), plt.yticks([])
plt.subplot(2,2,3),plt.imshow(edges2,cmap = 'gray')
plt.title('Edge Image 100x150'), plt.xticks([]), plt.yticks([])


plt.show()


cv2.imshow('Origin',res)
cv2.imshow('10x50 operation',edges)
cv2.imshow('100x150 operation',edges2)

cv2.waitKey(0)
cv2.destroyAllWindows()
