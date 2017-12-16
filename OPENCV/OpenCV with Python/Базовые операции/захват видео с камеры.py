import cv2

cap=cv2.VideoCapture(0)     #передаем адрес устройства
fps=30

#получаем размер
size=(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
#выделяем кодек для конвертации
fourcc = cv2.VideoWriter_fourcc(*'XVID')    #кодек для записи
#создаем экземпляр класса для записи видео
out = cv2.VideoWriter('outputWEB.avi',fourcc, 20.0, (640,480)) #выходной поток
#считываем поток видео
success,frame=cap.read()
numFrame=10*fps-1

while success and numFrame>0:
    out.write(frame)    #по кадравая запись
    success, frame = cap.read()     #считываем кадр
    c = cv2.waitKey(1)  # ожидание нажатия клавиши
    if c == 27:  # проверка клавиши ESC
        break
    cv2.imshow('Video', frame)



cap.release()
cv2.destroyAllWindows()

