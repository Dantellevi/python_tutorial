import cv2
import numpy as np

cap=cv2.VideoCapture(0)     #инициализация видео устройства

if  not cap.isOpened():     #проверка устройства
    raise IOError()

while True:
    ret,frame=cap.read()    #по кадровое считывание
    print(ret)
    print(frame)
    c=cv2.waitKey(1)        #ожидание нажатия клавиши
    if c==27:               #проверка клавиши ESC
        break

    cv2.imshow('Web Frame',frame)       #отображение

cap.release()
cv2.destroyAllWindows()