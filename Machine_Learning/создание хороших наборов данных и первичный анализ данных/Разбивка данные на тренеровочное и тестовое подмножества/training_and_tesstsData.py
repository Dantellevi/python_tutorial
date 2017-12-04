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

