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
#==================================================L1-регуляция(снижение сложности модели-уменьшение переобучения)===================================

from sklearn.linear_model import LogisticRegression
L1=LogisticRegression(penalty='l1',C=0.1)
L1.fit(X_train_std,y_train)

print('Верность на тренировочном наборе: ',L1.score(X_train_std,y_train))
print('Верность на тестовом наборе:',L1.score(X_test_std,y_test))

"""
Отмечаем для себя, что весовые векторы разрежены, т. е. имеют всего несколько 
ненулевых записей. В результате L1-регуляризации, которая служит в качестве ме­
тода отбора признаков, мы только что натренировали модель, устойчивую к потен­
циально нерелевантным (лишним) признакам в этом наборе данных. 
Наконец, построим график траекторий регуляризации,  т. е. весовых коэффициен­
тов, разных признаков для разных сил регуляризации: 
"""

import matplotlib.pyplot as plt

fig=plt.figure()
ax=plt.subplot(111)
colors=['blue','green','red','cyan',
        'magenta','yellow','black',
        'pink','lightgreen','lightblue',
        'gray','indigo','orange']

weights,params=[],[]
for c in np.arange(-4,6,dtype='float32'):
    lr=LogisticRegression(penalty='l1',C=10**c,random_state=0)
    lr.fit(X_train_std,y_train)
    weights.append(lr.coef_[1])
    params.append(10**c)

weights=np.array(weights)
for column, color in zip(range(weights.shape[1]),colors):
    plt.plot(params,weights[:,column],
             label=df_wine.columns[column+1],
             color=color)

plt.axhline(0,color='black',linestyle='--',linewidth=3)
plt.xlim([10**(-5),10**5])
plt.ylabel('Весовой коэффициент')
plt.xlabel('C')
plt.xscale('log')
plt.legend(loc='upper left')
ax.legend(loc='upper center',
          bbox_to_anchor=(0.5,1.03),
          ncol=1,fancybox=True)


plt.show()

#======================================================================================================================


