"""
Существенным преимуществом matplotlib является безбарьерная работа с LaTex. Нужно, чтобы в системе был установлена
 библиотека LaTeX (именно библиотека, а не редактор). Код LaTex оформляется в виде "raw" строки
  (перед строкой ставится символ r -> r'строка'). Также в настройках pyplot нужно указать, чтобы текст
  отрисовывался с учётом синтаксиса LaTeX. Это можно сделать через plt.rc('text', usetex=True).

"""

import matplotlib.pyplot as plt
import numpy as np


# Преамблуа для работы с LaTeX
plt.rc('text', usetex=True)


N = 100
x = np.arange(N)
z1 = np.cos(x/10.)
z2 = np.cos(x/20.)

fig = plt.figure()

plt.fill_between(x, z2, z1, color='green', alpha=0.25)      #закрашиваем внутреннюю область графика
plt.plot(x, z1, color='green', linewidth=4.0)
plt.plot(x, z2, color='green', linewidth=4.0, alpha=0.5)
plt.title(r'$\S1.3.2 \LaTeX example$')
plt.text(22, 0.5, r'$ e=mc^2 $', fontsize='16')
plt.text(55, -0.5, r'$\displaystyle\sum_{n=1}^\infty\frac{-e^{i\pi}}{2^n}$!', fontsize=18, rotation=60)

plt.grid(True)
plt.xlabel(r'\textbf{Time (s)}')
plt.ylabel(r'\textit{Sin(x) \& cos(x)}', color='red', rotation=45)


plt.show()

