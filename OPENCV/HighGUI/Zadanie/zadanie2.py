"""
	Реализуйте	возможность	рисования	(щелчок	левой	клавиши,	перемещение	и
отпускание	клавиши	мыши)	прямоугольника	на	изображении	при	помощи	мыши.
Будьте	осторожны,	сохраните	копию	исходного	изображения	в	памяти,	чтобы	не
испортить	его.	При	повторном	рисовании	ранее	созданный	прямоугольник
удаляется,	а	новый	рисуется	на	исходном	изображении.
b.	В	отдельном	окне	нарисуйте	график	количества	используемых	значений	синего,
зеленого	и	красного	каналов.	Ось	x	разбейте	на	8	блоков,	каждый	блок	должен
иметь	диапазон	в	32	значения:	0-31,	32-63,	...,	223-255.	Ось	y	должна	считать
количество	найденных	пикселей	в	данном	диапазоне.	Выполните	это	для	каждого
цветного	канала.


"""

import numpy as np
import  cv2
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
drawing=False
mode=True
ix,iy=-1,-1


def plot_graphics(y,x):
    marker='o'
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan', 'white', 'green', 'yellow')
    cmap = ListedColormap(colors[:len((np.unique(y)))])  # создаем палитрку


def read_image(name):
    img=cv2.imread(name)
    cv2.imshow('origin',img)
    return img



def draw_rectangle(event,x,y,flags,param):
    """метод рисования квадрата"""
    global ix, iy, drawing, mode  # глобальные переменные
    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y
    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            if mode==True:
                cv2.rectangle(edImg,(ix,iy),(x,y),(100,200,150),-1)
    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        if mode==True:
            cv2.rectangle(edImg, (ix, iy), (x, y), (100, 200, 150), -1)






if __name__=='__main__':
    edImg=read_image('images.jpg').copy()
    cv2.namedWindow('editImages')
    print(edImg.shape)
    cv2.setMouseCallback('editImages',draw_rectangle)

    while(1):
        cv2.imshow('editImages', edImg)
        cv2.imwrite('newImage.jpg',edImg)
        k=cv2.waitKey(1)
        if k==27:
            break


    cv2.destroyAllWindows()
