import cv2

image=cv2.imread('images.jpg')
cv2.imwrite('MyPic,jpg',image)

cv2.imshow('Images',image)
cv2.waitKey()
cv2.destroyAllWindows()
