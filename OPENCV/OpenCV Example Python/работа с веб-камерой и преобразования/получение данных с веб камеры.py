
import cv2

cap=cv2.VideoCapture(0)     #указываем устройства через которое будем работать

#Проверка на открытия устройства
if not cap.isOpened():
    raise IOError("Устройства не открывается!!!")

while True:
    ret,frame=cap.read()    #по кадровое считывания
    frame=cv2.resize(frame,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA) #уменьшаем изображение

    cv2.imshow('Input',frame)   #выводим ее в форму

    c=cv2.waitKey(1)    #ожидание нажатия на кнопку
    if c==27:
        break


cap.release()
cv2.destroyAllWindows() #очистка памяти

