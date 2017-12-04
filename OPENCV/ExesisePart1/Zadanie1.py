"""
Совместите	код	из	примера	2-11	и	код	из	примера	2-5,	чтобы	создать	программу,
которая	будет	считывать	видеопоток	с	камеры	и	сохранять	цветное	изображение	с
пониженной	дискретизацией	на	диск.


"""

import cv2
import numpy as np
Const_val=0.5

cap=cv2.VideoCapture(0)     #установка видео устройства
fourcc=cv2.VideoWriter_fourcc(*'XVID')      #применяемый кодек для AVI
outputFile=cv2.VideoWriter('output.avi',fourcc, 20.0, ((int)(640*Const_val),(int)(480*Const_val)))  #Потокавая запись

while (cap.isOpened()):
    ret,frame=cap.read()        #по кадровая чтение

    if ret == True:
        frame = cv2.resize(frame, None, fx=Const_val, fy=Const_val, interpolation=cv2.INTER_AREA)   #уменьшение размеров
        outputFile.write(frame)     #запись в поток
        cv2.imshow('Web Camera',frame)

        if cv2.waitKey(1)==27:
            break

    else:
        break

cap.release()
outputFile.release()
cv2.destroyAllWindows()