import cv2

img=cv2.imread('ImageTest.JPG')
img_scale=cv2.resize(img,None,fx=1.2,fy=1.2,interpolation=cv2.INTER_LINEAR) #произоводим изменение размеров(масштабирование)

cv2.imshow('Origin',img)
cv2.imshow('Img_resize',img_scale)

cv2.waitKey()
