import cv2
import numpy as np

img=cv2.imread('ImageTest.JPG')
rows,cols=img.shape[:2]

src_points=np.float32([[0,0],[cols-1,0],[0,rows-1]])        #точки для преобразования(три точки захвата исходного изображения)
#задаем положение точек для зеркального отображения
dst_points=np.float32([[cols-1,0],[0,0],[cols-1,rows-1]]) #точки для преобразования(положения где должны оказаться точки захвата)

affine_matrix=cv2.getAffineTransform(src_points,dst_points)     #генерируем матрицу преобразования
img_out=cv2.warpAffine(img,affine_matrix,(cols,rows))           #производим преобразование

cv2.imshow('Input',img)
cv2.imshow('OutPut',img_out)

cv2.waitKey()
