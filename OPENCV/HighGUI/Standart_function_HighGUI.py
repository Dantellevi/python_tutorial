import cv2

img=cv2.imread('Image.jpg')
cv2.namedWindow('Bicle')        #задает имя окна
cv2.moveWindow('Bicle',10,100)  #перемещает окно в указанные координаты
cv2.imshow('Bicle',img)
cv2.waitKey(0)
cv2.destroyAllWindows()