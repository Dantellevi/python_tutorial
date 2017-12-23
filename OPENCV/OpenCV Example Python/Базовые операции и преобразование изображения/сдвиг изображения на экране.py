import cv2
import numpy as np

img=cv2.imread('ImageTest.JPG') #открываем изображения
num_row,num_cols=img.shape[:2]  # считываем размер
"""
T= 
----------------------
   1 0 tx
   0 1 ty
----------------------

   
"""

translation_matrix=np.float32([[1,0,10],[0,1,10]]) #матрица преобразования для сдвига
translation_matrix_size=np.float32([[1,0,-30],[0,1,-50]]) #матрица преобразования для уменьшение размеров
img_translation_size=cv2.warpAffine(img,translation_matrix_size,(num_cols+70+30,num_row+110+50))
img_translation=cv2.warpAffine(img,translation_matrix,(num_cols,num_row))   #Аффиново преобразование сдвиг
cv2.imshow('Origin',img)
cv2.imshow('Translation',img_translation)
cv2.imshow('Translation_Size',img_translation_size)
cv2.waitKey()



