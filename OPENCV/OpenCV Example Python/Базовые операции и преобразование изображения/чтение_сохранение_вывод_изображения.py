import cv2


img=cv2.imread('ImageTest.JPG') #открываем изображение
cv2.imshow('Input Image',img)   #выводим его на экран
cv2.waitKey()       #ожидаем нажатия клавиши


