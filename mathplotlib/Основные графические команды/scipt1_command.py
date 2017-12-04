"""
Самые простые графические команды:

plt.scatter() - маркер или точечное рисование;

plt.plot() - ломаная линия;

plt.text() - нанесение текста;

II. Диаграммы:

plt.bar(), plt.barh(), plt.barbs(), broken_barh() - столбчатая диаграмма;

plt.hist(), plt.hist2d(), plt.hlines - гистограмма;

plt.pie() - круговая диаграмма;

plt.boxplot() - "ящик с усами" (boxwhisker);

plt.errorbar() - оценка погрешности, "усы".

III. Изображения в изолиниях:

plt.contour() - изолинии;

plt.contourf() - изолинии с послойной окраской;

IV. Отображения:

plt.pcolor(), plt.pcolormesh() - псевдоцветное изображение матрицы (2D массива);

plt.imshow() - вставка графики (пиксели + сглаживание);

plt.matshow() - отображение данных в виде квадратов.

V. Заливка:

plt.fill() - заливка многоугольника;

plt.fill_between(), plt.fill_betweenx() - заливка между двумя линиями;

VI. Векторные диаграммы:

plt.streamplot() - линии тока;

plt.quiver() - векторное поле.


"""


import  matplotlib.pyplot as plt

fig=plt.figure()
# Добавление на рисунок прямоугольной (по умолчанию) области рисования
scatter1=plt.scatter(0.0,1.0)

print('Scatter:',type(scatter1))
graph1=plt.plot([-1.0,1.0],[0.0,1.0])
print('Plot:',len(graph1),graph1)
text1 = plt.text(0.5, 0.5, 'Text on figure')
print('Text: ', type(text1))

grid1 = plt.grid(True)   # линии вспомогательной сетки

plt.show()


