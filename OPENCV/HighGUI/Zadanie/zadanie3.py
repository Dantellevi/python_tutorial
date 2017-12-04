"""
Напишите	программу,	которая	создает	изображение	(белое	полотно),
устанавливает	все	значения	в	0	и	отображает	результат
	на	экране.
	Обеспечьте
возможность	рисовать	линии,	круги,	эллипсы	и	полигоны,
	используя	левую
клавишу	мыши.
Создайте	функцию	"ластик",	которая	будет	вызываться	при
нажатии	правой	клавиши	мыши.


"""

import numpy as np

import cv2

drawing=False
mode=True
ix,iy=-1,-1
drC=False
mC=False
ixC=-1
iyC=-1

flagfigure=0

def draw_rectangle(event,x,y,flags,param):
    global ix, iy, drawing, mode  # глобальные переменные

    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y

    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            if mode==True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)


    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        if mode==True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)



def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv2.circle(img,(x,y),5,(0,0,255),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
        else:
            cv2.circle(img,(x,y),5,(0,0,255),-1)






if __name__=='__main__':
    img = np.zeros((512, 512, 3), np.uint8)  # создаем матрицу изображения
    img[:,:]=255
    cv2.namedWindow('image')



    while(1):
        cv2.imshow('image',img)
        if cv2.waitKey(33) == ord('q'):
            print('рисуем квадрат')
            flagfigure = 1
        elif cv2.waitKey(33) == ord('w'):
            flagfigure = 2
            print('рисуем круг')
        elif cv2.waitKey(33) == ord('r'):
            flagfigure = 3
            print('рисуем треугольник')

        if flagfigure == 1:
            cv2.setMouseCallback('image', draw_rectangle)
        elif flagfigure==2:
            cv2.setMouseCallback('image',draw_circle)










        if cv2.waitKey(1)==27:
            break



    cv2.destroyAllWindows()
