#	Простая	программа	для	воспроизведения	видеофайла	с	диска

import cv2

cap=cv2.VideoCapture('video1.mp4')      #считываем видео файл

while True:
    ret,frame=cap.read()                #покадровое считывание

    if frame==None:                     #конец файла
        break

    cv2.imshow("Video Frame",frame)     #вывод видео

    c=cv2.waitKey(1)                    #нажатие клавиши

    if c==27:                           #проверка
        break


cap.release()                           #очистка буфера и ОЗУ
cv2.destroyAllWindows()                 #удаление окна





