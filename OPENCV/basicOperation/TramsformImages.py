#Загрузка	и	сглаживание	изображения	с	последующим	отображением
#результата	на	экране

import cv2
import numpy as np

#функция преобразование(размытия)
def Transform(image):
    image=cv2.resize(image,None,fx=0.3,fy=0.3,interpolation=cv2.INTER_AREA) #уменьшаем размер изображения
    kernel=np.ones((5,5),np.float32)/25 #создаем ядро для преобразования
    print(kernel)
    dst=cv2.filter2D(image,-1,kernel)   #преобразование методом усреднения
    blur=cv2.GaussianBlur(image,(5,5),0)    #Гауссовское размытие

    cv2.imshow('Averaging',dst)             #отображение
    cv2.imshow('GausianBlur', blur)         #отображение
    cv2.imshow('Original', image)           #отображение
    cv2.waitKey(0)                          #ожидание нажатия клавиши
    cv2.destroyAllWindows()                 #уничтожение всех окон


if __name__=='__main__':
    img = cv2.imread('Image.jpg')
    Transform(img)



