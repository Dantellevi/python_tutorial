import cv2

img=cv2.imread('images.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('Gray',img)
cv2.waitKey()
cv2.destroyAllWindows()
