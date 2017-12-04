# постройка графика с настройками
import numpy as np
import matplotlib.pyplot as plt

x=np.linspace(-123,12,75)

y=np.sin(x)/x
"""настройка вида производится:
цвета (одна из букв rgbymcwk)
• вида линии (- -- -. :)
• маркера (один из символов .,oˆv<>s+xDd1234hHp|_)

"""
plt.plot(x,y,'b-^')
plt.show()

