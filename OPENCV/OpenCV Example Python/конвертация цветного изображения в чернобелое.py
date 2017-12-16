import cv2


img=cv2.imread('ImageTest.JPG') #читаем изображение
print(img.shape)                #выводим размерность
print('---------------------------------------')
print(img)                      #выводим многомерный массив

gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)   #конвертируем в чернобелый
cv2.imshow('Gray image',gray_img)               #выводим в окно
cv2.waitKey()

