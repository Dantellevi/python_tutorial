import cv2

img=cv2.imread('Image.JPG',cv2.IMREAD_GRAYSCALE)


"""
Функция фильтрации Шарра используется для аппроксимациия(взятие производной) по определенной оси(может использоваться как для мелких так и для крупных ядер)
cv2.Scharr(src,dst,depth,xorder,yorder)

src-исходное изображение
dst-полученное изображение
depth-размерность,глубина выходного изображения
xorder-степень производной по х
yorder-степень производной по у

"""
ScharrX=cv2.Scharr(img,cv2.CV_64F,1,0)
ScharrY=cv2.Scharr(img,cv2.CV_64F,0,1)



cv2.imshow('Origin',img)
cv2.imshow('SobelX',ScharrX)
cv2.imshow('SobelY',ScharrY)


cv2.waitKey(0)
cv2.destroyAllWindows()
