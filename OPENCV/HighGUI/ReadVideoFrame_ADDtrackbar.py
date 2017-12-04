#считывания видео файла и добавление трекбара

import cv2



cap=cv2.VideoCapture('video1.mp4')      #чтение файла

g_capture=None

def onChange(trackbarValue):
    cap.set(cv2.CAP_PROP_POS_FRAMES,trackbarValue)  #установка значения с трекбара
    err,img = cap.read()                            #считывание видеопотока по кадрово
    cv2.imshow("mywindow", img)                     #отображение
    pass

length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))     #получение длинны фрейма
cv2.namedWindow('mywindow')                         #установка названия окна
cv2.createTrackbar( 'start', 'mywindow', 0, length, onChange )  #создаем трекбар
# cv2.createTrackbar( 'end'  , 'mywindow', 100, length, onChange )
onChange(0) #установка начального значения
cv2.waitKey()   #ожидание

start = cv2.getTrackbarPos('start','mywindow')      #получение стартового значения
end  = cv2.getTrackbarPos('end','mywindow')         #получение конечного значения
# if start >= end:
#     raise Exception("start must be less than end")

cap.set(cv2.CAP_PROP_POS_FRAMES,start)              #устанавливаем значение видео фрейма

while cap.isOpened():
    err, img = cap.read()
    if cap.get(cv2.CAP_PROP_POS_FRAMES) >= end:     #если отстутствуют кадры прервать
        break
    cv2.imshow("mywindow", img)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break



cap.release()
cv2.destroyAllWindows()
