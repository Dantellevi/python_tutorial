"""
Плавная цветовая палитра представляет собой
результат линейной интерполяции между
последовательностью цветов, составляющих
основу палитры.

Различные методы отображения трёхмерных
данных (разные графические команды) по умолчанию
используют разные типы цветовых палитр.
Так методы plt.imshow() и plt.pcolor() будут
сопровождаться плавной цветовой палитрой:
"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

dat = np.random.random(200).reshape(20,10) # создаём матрицу значений

# Создаём список цветовых палитр из словаря
maps = [m for m in plt.cm.datad]

fig, axes = plt.subplots(nrows=2, ncols=1, sharex=True)  # смотри главу "Рисунки с несколькими областями рисования"

cmaplist = plt.cm.datad

for i, ax in enumerate(fig.axes):
    random_cmap = np.random.choice(maps)
    if (i == 0):
        cf = ax.pcolor(dat, cmap=plt.get_cmap(random_cmap))
    else:
        cf = ax.imshow(dat, cmap=plt.get_cmap(random_cmap))

    ax.set_title('%s colormap' % random_cmap)

    fig.colorbar(cf, ax=ax)

plt.suptitle(u'Различные цветовые палитры')
plt.show()

