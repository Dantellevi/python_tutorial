import cv2

img=cv2.imread('Image.JPG',cv2.IMREAD_GRAYSCALE)


"""
Функция оператора Собеля используется для аппроксимациия(взятие производной) по определенной оси(в основном используется для крупных ядер)
cv2.Sobel(src,dst,depth,xorder,yorder,aperture_size=3)

src-исходное изображение
dst-полученное изображение
depth-глубина выходного изображения
xorder-степень производной по х
yorder-степень производной по у
aperture_size-нечетное число задает ширину и высоту квадратного фильтра
"""
sobelX=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobelY=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)



cv2.imshow('Origin',img)
cv2.imshow('SobelX',sobelX)
cv2.imshow('SobelY',sobelY)


cv2.waitKey(0)
cv2.destroyAllWindows()
