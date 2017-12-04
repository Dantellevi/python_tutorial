"""
Преобразует карты преобразования изображений из одного представления в другое.

Python: cv2.convertMaps( map1, map2, dstmap1type [ , dstmap1 [ , dstmap2 [ , nninterpolation ] ] ] ) → dstmap1, dstmap2
Параметры:
map1 - Первый вход отображение типа CV_16SC2 , CV_32FC1или CV_32FC2.
map2 - Второй вход карта типа CV_16UC1 , CV_32FC1 или нет (пустая матрица), соответственно.
dstmap1 - первая карта вывода, которая имеет тип dstmap1type и тот же размер, что и src.
dstmap2 - вторая карта вывода.
dstmap1type - Тип первой выходной карты , которая должна быть CV_16SC2, CV_32FC1или CV_32FC2.
nninterpolation - флаг, указывающий, используются ли карты с фиксированной точкой для ближайшего соседа или для более сложной интерполяции.


изменение перспективы
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('Image.JPG')
rows,cols,ch = img.shape

pts1 = np.float32([
    [315, 15],
    [962, 18],
    [225, 701],
    [1036, 694],
], dtype=int)

pts2 = np.float32([
     [14, 14],
     [770, 14],
     [14, 770],
     [770, 770]
], dtype=int)

M = cv2.getPerspectiveTransform(pts1,pts2)

dst = cv2.warpPerspective(img,M,(784,784))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()

