"""
В силу вышесказанного существуют два общих подхода к приведению разных
признаков к одинаковой шкале: нормализация и стандартизация. В различных об­
ластях эти термины нередко используются довольно нечетко, и их конкретное со­
держание приходится выводить из контекста. Чаще всего нормализация означает
приведение (нормирование) признаков к диапазону [О, 1]  и является частным слу­
чаем минимаксного масштабирования.  Для нормализации наших данных можно
к каждому признаковому столбцу просто применить минимаксное масштабирова­
ние, где новое значение x~2rm из образца x<i)


Процедура минимаксного масштабирования реализована в  библиотеке scikit-
leaш и может быть применена следующим образом:
from  sklearn.preprocessing  import  MinMaxScaler
mms =MinMaxScaler()
X_train_norm=mms.fit_transform(X_train)
X_test_norm=mms.transform(X_test)
===========================================================
При помощи стандартизации мы центрируем признаковые столбцы
в нулевом среднем значении, т. е. равном О, с единичным стандартным отклонением,
т. е. равным 1, в результате чего признаковые столбцы принимают вид нормального
распределения, что упрощает извлечение весов.  Кроме того, стандартизация содер­
жит полезную информацию о выбросах и делает алгоритм менее к ним чувстви­
тельным, в отличие от минимаксного масштабирования, которое шкалирует данные
в ограниченном диапазоне значений.

Помимо класса  минимаксного  масштабирования  MinMaxScaler,  в  библиотеке
scikit-leaгn также реализован класс стандартизации StandardScaler:
from  sklearn . preprocessing  i mport  StandardScaler
stdsc  =  StandardScaler ()
X_ train _std  =  stdsc .fit _ trans f orm (X_  t r ain)
X_tes t_std =  stdsc. transform(X_tes t)

"""

import pandas as pd
import numpy as np


url='https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'

df_wine=pd.read_csv(url,header=None)    #считываем набор данных вин для проведения исследования

df_wine.columns=['Метка класса','Алкоголь',
                 'Яблочная кислота', 'Зола',
                 'Щелочность золы','Магний',
                 'Всего фенола','Флаваноиды',
                 'Фенолы нефлаваноидные','Проантоцианины',
                 'Интенсивность цвета','Оттенок',
                 'OD280/OD315 разбавленныех вин','Пролин']
print('Метки классов:',np.unique(df_wine['Метка класса']))
df_wine.head()

"""
Функция train_test_split из подмодуля отбора модели model_selection  библиоте­
ки scikit-leaгn (в версии библиотеки< 0.18 этот модуль назывался cross_validation) 
предоставляет удобный способ случайным образом разделить этот набор данных на 
отдельные тестовый и тренировочный наборы данных: 
"""

from sklearn.model_selection import train_test_split


"""
Сначала мы присвоили переменной Х представленные в виде массива NumPy 
признаковые столбцы 1-13, а переменной у присвоили метки классов из первого 
столбца. Затем мы применили функцию train_test_split,  чтобы случайным образом 
разделить Х и у на отдельные тренировочный и тестовый наборы данных.  Установив 
параметр test_size=O.З, мы присвоили 30%  образцов вин массивам X_test  и y_test 
и оставшиеся 70% образцов - соответственно массивам X_train и y_train. 

"""
X,y=df_wine.iloc[:,1:].values,df_wine.iloc[:,0].values
X_train,X_test,y_train,y_test=\
train_test_split(X,y,test_size=0.3,random_state=0)


#===================================Нормализация данных===============================
from  sklearn.preprocessing  import  MinMaxScaler
mms =MinMaxScaler()
X_train_norm=mms.fit_transform(X_train)
X_test_norm=mms.transform(X_test)
print(X_test_norm)
print('----------------------------------------------')
print(X_train_norm)
print('####################################################################################')
#======================================Стандартизация===============================
from  sklearn . preprocessing  import StandardScaler
stdsc  =  StandardScaler ()
X_train_std  = stdsc.fit_transform (X_train)
X_test_std =  stdsc. transform(X_test)

print(X_test_std)
print('----------------------------------------------')
print(X_train_std)
print('####################################################################################')

#====================================================================================