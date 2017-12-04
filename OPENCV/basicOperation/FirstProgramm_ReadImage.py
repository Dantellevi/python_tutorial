#Простая	OpenCV	программа	-	загрузка	изображения	с	диска	и
#отображение	его	на	экране
import cv2

img=cv2.imread("Image.jpg")     #получение изображения

img=cv2.resize(img,None,fx=0.1,fy=0.1,interpolation =cv2.INTER_AREA)    #уменьшение размеров
cv2.imshow("Image Fist",img)                                            #вывод изображения
cv2.waitKey(0)              #ожидание кнопки закрытия

cv2.destroyAllWindows()     #удаление окна


