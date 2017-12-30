import cv2
import argparse


def argument_parser():
    parser=argparse.ArgumentParser(description="Выберетие цвет входного потока изображения используя клавиатуру. Контрольные кнопки : GrayScale: g,YUV-y, HSV:h")
    return parser



if __name__=="__main__":
    args=argument_parser().parse_args()

    cap=cv2.VideoCapture(0)

    #Проверка устройства
    if not cap.isOpened():
        raise IOError("Ошибка!!Камера не найдена!!!")

    cur_char=-1
    prev_char=-1
    c=0
    while True:
        #читаем одельный кадр из потока
        ret,frame=cap.read()

        #уменьшаем изображения
        frame=cv2.resize(frame,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)

        c = cv2.waitKey(10)
        if c == 27:
            break
        if c != prev_char:
            cur_char = c
            prev_char = c


        if cur_char==ord('g'):
            output = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('Webcam', output)

        elif cur_char==ord('y'):
            output=cv2.cvtColor(frame,cv2.COLOR_BGR2YUV)
            cv2.imshow('Webcam', output)
        elif cur_char==ord('h'):
            output=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
            cv2.imshow('Webcam', output)
        else:
            output=frame
            cv2.imshow('Webcam', output)





    cap.release()
    cv2.destroyAllWindows()





