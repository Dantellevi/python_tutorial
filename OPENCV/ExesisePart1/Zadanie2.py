"""
Модифицируйте	предыдущий	код	добавлением	в	него	слайдера	из	примера	2-3,
чтобы	пользователь	смог	динамически	изменять	пирамидальное	размытие	между
2	и	8.	Можно	опустить	этап	записи	результата	на	диск.	(Судя	по	всему	речь	идет	об
изменении	третьего	аргумента	функции	pyrDown()	при	помощи	функции	Size().
Прототип	pyrDown(const	CvArr	src,	CvArr	dst,	int	filter=CV_GAUSSIAN_5x5).	Как
результат,	чем	выше	показатель,	тем	более	размытым	будет	изображение)

"""



import cv2
import numpy as np

def onChange(trackbarValue):
    global trackval
    if trackbarValue%2!=0:
        trackval = trackbarValue

    pass


def Transform(frames):
     blur = cv2.GaussianBlur(frames, (trackval, trackval), 0)
     return blur


if __name__=='__main__':
    g_capture = None
    cap=cv2.VideoCapture(0)
    cv2.namedWindow('Transform')
    cv2.createTrackbar('start', 'Transform', 1, 99, onChange)

    global ret, frame
    ret,frame=None,None
    onChange(1)  # установка начального значения
    #cv2.waitKey()  # ожидание

    start = cv2.getTrackbarPos('start', 'Transform')  # получение стартового значения
    end = cv2.getTrackbarPos('end', 'Transform')
    while cap.isOpened():

        ret,frame=cap.read()
        frame = cv2.resize(frame, None, fx=0.7, fy=0.7, interpolation=cv2.INTER_AREA)
        frame=Transform(frame)
        cv2.imshow('Transform',frame)
        k = cv2.waitKey(10) & 0xff
        if k == 27:
            break

    cap.release()
    cv2.destroyAllWindows()




