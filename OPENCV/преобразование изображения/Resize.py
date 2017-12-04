
import cv2
import numpy as np

im_in=cv2.imread('Image.JPG')
res=cv2.resize(im_in,None,fx=2,fy=2,interpolation=cv2.INTER_AREA)

cv2.imshow('origin',im_in)
cv2.imshow('Resize Image',res)

cv2.waitKey()
cv2.destroyAllWindows()
