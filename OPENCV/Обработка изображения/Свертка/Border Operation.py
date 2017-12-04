import numpy as np
import cv2
import matplotlib.pyplot as plt

img1=cv2.imread('Origin.JPG')

BLUE = [255,0,0]
"""
сли вы хотите создать границу вокруг изображения, что-то вроде фоторамки, вы можете использовать функцию cv2.copyMakeBorder () . Но у него больше приложений для операции свертки, нулевого заполнения и т. Д. Эта функция принимает следующие аргументы:

src - входное изображение
верхняя , нижняя , левая , правая границы в количестве пикселей в соответствующих направлениях
borderType - флаг, определяющий, какую границу нужно добавить. Это могут быть следующие типы:
cv2.BORDER_CONSTANT - добавляет постоянную цветную рамку. Значение должно быть указано в следующем аргументе.
cv2.BORDER_REFLECT - Граница будет зеркальным отражением элементов границы, например: fedcba | abcdefgh | hgfedcb
cv2.BORDER_REFLECT_101 или cv2.BORDER_DEFAULT - То же, что и выше, но с небольшими изменениями, например: gfedcb | abcdefgh | gfedcba
cv2.BORDER_REPLICATE - последний элемент реплицируется повсюду, например: aaaaaa | abcdefgh | hhhhhhh
cv2.BORDER_WRAP - Не могу объяснить, это будет выглядеть так: cdefgh | abcdefgh | abcdefg
value - Цвет границы, если тип границы - cv2.BORDER_CONSTANT
"""
replicate = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REPLICATE)   #создаем новую картинку из старой с учетом границ
reflect = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img1,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()