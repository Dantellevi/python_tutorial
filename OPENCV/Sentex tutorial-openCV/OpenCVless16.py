import cv2
import numpy as np

#Обнаружение объектов
#загружаем данные для классификации лица
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#подгружаем данные для классификации глаз
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
#получаем видео поток
cap=cv2.VideoCapture(0)
while True:
    #передаем видео поток
    ret,img=cap.read()

    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    #Обнаруживает объекты разных размеров во входном изображении.
    # Обнаруженные объекты возвращаются как список прямоугольников.
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        #построение прямоуголльников вокруг обнаруженных объектах
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = img[y:y + h, x:x + w]

        eyes=eye_cascade.detectMultiScale(roi_gray)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    cv2.imshow('img',img)






cap.release()
cv2.destroyAllWindows()