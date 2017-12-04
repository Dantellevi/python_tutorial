#импортируем библиотеку
import cv2

src=cv2.imread('threshold.JPG',cv2.IMREAD_GRAYSCALE)

# Set threshold and maxValue
thresh = 0
maxValue = 100

th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY_INV)

cv2.imshow('threshold-INVERT',dst)
cv2.waitKey()
cv2.destroyAllWindows()