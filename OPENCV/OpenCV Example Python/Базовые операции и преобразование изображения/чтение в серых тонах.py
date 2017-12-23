import cv2
import numpy as np
gray_img=cv2.imread('ImageTest.JPG',cv2.IMREAD_GRAYSCALE)   #читаем изображение в серых тонах
print(gray_img.shape)
cv2.imshow('Gray',gray_img)     #выводим изображение на экран

cv2.waitKey()                   #ожидаем нажатие кнопки
cv2.imwrite('outImage.jpg',gray_img)    #сохраняем изображение




