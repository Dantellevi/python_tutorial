"""
 Загрузите	любое	изображение	и	размойте	его	с	помощью	cvSmooth()	с	smoothtype
=	CV_GAUSSIAN.
a.	Используйте	симметричную	область	сглаживания	3x3,	5x5,	9x9,	11x11	и
выведите	результаты	на	экран.
b.	Одинаковы	ли	результаты	двойного	сглаживания	изображения	с	областью	5x5	и
с	областью	11x11.	Почему	да	или	почему	нет?

"""


import cv2
import numpy as np


img=cv2.imread('originImg.JPG')

blur=cv2.GaussianBlur(img,(3,3),0)
blur5x5=cv2.GaussianBlur(img,(5,5),0)
blur9x9=cv2.GaussianBlur(img,(9,9),0)
blur11x11=cv2.GaussianBlur(img,(11,11),0)
cv2.imshow('Smoothing 3x3',blur)
cv2.imshow('Smoothing 5x5',blur5x5)
cv2.imshow('Smoothing 9x9',blur9x9)
cv2.imshow('Smoothing 11x11',blur11x11)
cv2.imshow('origin',img)
cv2.waitKey()
cv2.destroyAllWindows()
