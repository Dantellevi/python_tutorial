"""
Последовательность или набор цветов образует цветовую
палитру colormap. Чаще всего она используется при
отрисовке трёхмерных данных. Но и автоматический подбор
цветов при добавлении каждого нового экземпляра plot
также осуществляется из цветовой палитры по умолчанию.

Для получения текущей цветовой палитры можно воспользоваться
методом plt.get_cmap('название палитры').
Список всех предустановленных палитр можно получить с
помощью метода plt.cm.datad. В настройках matplotlibrc
можно также изменить цветовую палитру с помощью параметра
image.cmap. В интерактивном режиме её можно поменять через
plt.rcParams['image.cmap']='имя_палитры' или через
plt.set_cmap('имя_палитры'). Последний позволяет изменить
палитру текущего рисунка уже после вызова графических команд.

"""

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

dat=np.random.random(200).reshape(20,10) # создаём матрицу значений

#создаем список цветовых палитр из словаря
maps=[m for m in plt.cm.datad]

print(u'Предустановленные цветовые палитры:', maps)

fig,axes=plt.subplots(nrows=2,ncols=2,sharex=True,sharey=True)

cmaplist = plt.cm.datad

for ax in fig.axes:
    random_cmap = np.random.choice(maps)    #генерируем различные цветовые варианты
    cf = ax.contourf(dat, cmap=plt.get_cmap(random_cmap))   #наносим цветовые варианты на отдельрые полотна внутри главного полотна
    ax.set_title('%s colormap' % random_cmap)
    fig.colorbar(cf, ax=ax) #выводим цветовые названия

plt.suptitle(u'Различные цветовые палитры')   # единый заголовок рисунка
plt.show()

