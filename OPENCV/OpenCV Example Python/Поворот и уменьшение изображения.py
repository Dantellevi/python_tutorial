import cv2
import numpy as np

img=cv2.imread('ImageTest.JPG')
num_rows,num_cols=img.shape[:2]

translation_matrix=np.float32([[1,0,int(0.5*num_cols)],[0,1,int(0.5*num_rows)]])    #генерируем матрицу преобразования дял уменьшение
rotation_matrix=cv2.getRotationMatrix2D((num_cols,num_rows),30,1)                   #поворот изображения
img_translation=cv2.warpAffine(img,translation_matrix,(2*num_cols,2*num_rows))      #уменьшение размеров
img_rotation=cv2.warpAffine(img_translation,rotation_matrix,(2*num_cols,2*num_rows))    #преобразовываем для поворота

cv2.imshow('Rotation',img_rotation)
cv2.waitKey()



