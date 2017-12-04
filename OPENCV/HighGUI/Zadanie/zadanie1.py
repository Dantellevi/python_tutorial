"""

Напишите	программу,	которая:	(1)	читает	кадры
	из	видеофайла,	(2)
конвертирует	получаемые	кадры
	в	черно-белый	формат

	Добавить текстовые заметки


"""

import numpy as np
import cv2

cap=cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX

while cap.isOpened():
    ret,frame=cap.read()
    framegray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.putText(framegray, 'Convert to Gray Frame', (10, 100), font, 1, (255, 255, 255), 2, cv2.LINE_AA)
    cv2.imshow('gray',framegray)
    cv2.imshow('origin',frame)

    if cv2.waitKey(1)==27:
        break


cap.release()

cv2.destroyAllWindows()

