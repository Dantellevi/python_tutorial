#импортируем библиотеку
import cv2

src=cv2.imread('threshold.JPG',cv2.IMREAD_GRAYSCALE)

# Set threshold and maxValue
thresh = 180
maxValue = 255

# Basic threshold example
th, dst = cv2.threshold(src, thresh, maxValue, cv2.THRESH_BINARY)

cv2.imshow('threshold',dst)
cv2.waitKey()
cv2.destroyAllWindows()