#Запись	видео	в	формате	AVI

import  cv2
import numpy as np

cap=cv2.VideoCapture(0)                 #устанавливаем видео устройство
fourcc = cv2.VideoWriter_fourcc(*'XVID')    #кодек для записи

out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480)) #выходной поток


while (cap.isOpened()):
    ret,frame=cap.read()    #по кадровое считывание
    if ret==True:
        frame=cv2.flip(frame,0)     #переворачиваем изображение

        out.write(frame)            #записываем кадр в выходной файл
        cv2.imshow('frame',frame)

        if (cv2.waitKey(1))==27:
            break

    else:
        break



cap.release()
out.release()
cv2.destroyAllWindows()
