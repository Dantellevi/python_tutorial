import cv2

videoCapture=cv2.VideoCapture('video1.mp4')
fps=videoCapture.get(cv2.CAP_PROP_FPS)


size=(int(videoCapture.get(3)),
      int(videoCapture.get(4)))

fourcc = cv2.VideoWriter_fourcc(*'XVID')    #кодек для записи
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480)) #выходной поток
success,frame=videoCapture.read()
while success:#Пока имеются данные в фрейме проходим по циклу
    out.write(frame)
    success,frame=videoCapture.read()
    c = cv2.waitKey(1)  # ожидание нажатия клавиши
    if c == 27:  # проверка клавиши ESC
        break
    cv2.imshow('Video',frame)



videoCapture.release()
cv2.destroyAllWindows()