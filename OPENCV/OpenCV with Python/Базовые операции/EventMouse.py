"""
Игрушечная	программа,	использующая	мышь	для	рисования
прямоугольника


"""

import cv2
import numpy as np

drawing=False
mode=True
ix,iy=-1,-1


def draw_rectangle(event,x,y,flags,param):
    """метод рисования квадрата"""
    global ix, iy, drawing, mode        #глобальные переменные
    if event == cv2.EVENT_LBUTTONDOWN:  #событие нажатие кнопки
        drawing = True
        ix, iy = x, y
    elif event==cv2.EVENT_MOUSEMOVE:    #собитые перемещение мыши
        if drawing==True:
            if mode==True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)   #рисуем квадрат


    elif event==cv2.EVENT_LBUTTONUP:    #событие отжатия мыши
        drawing=False
        if mode==True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)   #рисуем квадрат











if __name__=="__main__":
    img=np.zeros((512,512,3),np.uint8)  #создаем матрицу изображения
    cv2.namedWindow('image')            #задаем имя изображения
    cv2.setMouseCallback('image',draw_rectangle)    #подписываемся на события

    while(1):
        cv2.imshow('image',img)
        k=cv2.waitKey(1)

        if k==27:
            break

    cv2.destroyAllWindows()
