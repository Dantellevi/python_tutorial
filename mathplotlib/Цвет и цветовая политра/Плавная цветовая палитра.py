import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np

dat = np.random.random(200).reshape(20,10) # создаём матрицу значений

xx = np.array([0.5, 0.0, 0.1])*255
print(xx)
# Создаём список цветовых палитр из словаря

# ---------------------------------------------------------
# Вариант 1 Ромашка (бело-жёлтый)

cdict1 = {'red':   ((0.0, 1.0, 1.0),
                   (1.0, 1.0, 1.0)),

         'green': ((0.0, 1.0, 1.0),
                   (1.0, 1.0, 1.0)),

         'blue':  ((0.0, 1.0, 1.0),
                   (1.0, 0.0, 0.0))
        }

cmap1 = mpl.colors.LinearSegmentedColormap('cmap1', cdict1)


# Вариант 2 Светофор(красный-жёлтый-зелёный)

cdict2 = {'red':   ((0.0, 0.0, 0.0),
                   (0.5, 1.0, 1.0),
                   (1.0, 1.0, 1.0)),

         'green': ((0.0, 1.0, 1.0),
                   (0.5, 1.0, 1.0),
                   (1.0, 0.0, 0.0)),

         'blue':  ((0.0, 0.0, 0.0),
                   (0.5, 0.0, 0.0),
                   (1.0, 0.0, 0.0))
        }

cmap2 = mpl.colors.LinearSegmentedColormap('cmap2', cdict2)
# ---------------------------------------------------------

fig, axes= plt.subplots(nrows=2, ncols=1, sharex=True)

cmaplist = plt.cm.datad

cmaps = [cmap1, cmap2]

for i, ax in enumerate(fig.axes):
    cf = ax.imshow(dat, cmap=cmaps[i])
    fig.colorbar(cf, ax=ax)

plt.suptitle(u'Создание цветовых палитр')
plt.show()
