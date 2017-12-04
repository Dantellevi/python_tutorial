import cv2
import numpy as np

#считываем изображения
im_in=cv2.imread('Fill.JPG',cv2.IMREAD_GRAYSCALE)

#Пороговое сравнение.
# Установите значения, равные или выше 220 на 0.
# Установите значения ниже 220 - 255.

th, im_th = cv2.threshold(im_in, 220, 255, cv2.THRESH_BINARY_INV);

#Делаем копию
im_floodfill=im_th.copy()

# Маска используется для заливки.
# Обратите внимание, что размер должен быть 2 пикселя, чем изображение
h, w = im_th.shape[:2]
mask = np.zeros((h+2, w+2), np.uint8)

cv2.floodFill(im_floodfill,mask,(0,0),255)
# Инвертировать залитое изображение
im_floodfill_inv = cv2.bitwise_not(im_floodfill)

# Объедините два изображения, чтобы получить передний план.
im_out = im_th | im_floodfill_inv

# Display images.
cv2.imshow("Thresholded Image", im_th)
cv2.imshow("Floodfilled Image", im_floodfill)
cv2.imshow("Inverted Floodfilled Image", im_floodfill_inv)
cv2.imshow("Foreground", im_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
