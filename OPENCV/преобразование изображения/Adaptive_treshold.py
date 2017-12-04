import cv2

import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('Addaptive_threshold.JPG',0)
img=cv2.medianBlur(img,5)        #производим размытие

ret,th1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)          #обычное пороговое преобразование
th2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)                             #адаптивная пороговое преобразование
th3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)                             #гаусовское адаптивное пороговое преобразование

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']     #кортеж заглавий
images = [img, th1, th2, th3]                                                   #кортеж изображений

for i in range(4):                                                              #вывод нескольких изображений на одно полотно
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()