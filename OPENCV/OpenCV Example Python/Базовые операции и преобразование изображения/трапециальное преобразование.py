import cv2
import numpy as np

img=cv2.imread('ImageTest.JPG')
rows,cols=img.shape[:2]
src_points=np.float32([[0,0],[cols-1,0],[0,rows-1],[cols-1,rows-1]])        #исходные точки для преобразования
dst_points=np.float32([[0,0],[cols-1,0],[int(0.33*cols),rows-1],[int(0.66*cols),rows-1]])   #конечные точки для преобразования

projective_matrix=cv2.getPerspectiveTransform(src_points,dst_points)
img_output=cv2.warpPerspective(img,projective_matrix,(cols,rows))

cv2.imshow('Input',img)
cv2.imshow('Perspective Transform',img_output)

cv2.waitKey()


