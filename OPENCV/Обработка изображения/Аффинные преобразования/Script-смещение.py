import cv2
import numpy as np

img=cv2.imread('Image.JPG',0)
rows,cols=img.shape

#матрица преобразования  M[[растяжение по y,растяжение по диагонали,смещение по х],[отклонение по z,растяжение по диагонали,смещение по у]]
M=np.float32([[1,10,10],[0,10,10]])

dst=cv2.warpAffine(img,M,(cols,rows))

cv2.imshow('origin',img)
cv2.imshow('Affine transform-smeshenie',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
