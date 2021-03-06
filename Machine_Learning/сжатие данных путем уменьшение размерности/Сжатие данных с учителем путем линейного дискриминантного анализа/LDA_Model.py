"""
Линейный дискриминантный анализ (lineaг discгiminant analysis,  LDA), он же ка­
нонический, может использоваться в качестве метода для выделения признаков
в целях увеличения вычислительной эффективности и уменьшения степени пере­
подгонки из-за проблемы проклятия размерности в нерегуляризованных моделях.
В основе LDA лежит общая идея, которая очень похожа на РСА.  Правда, РСА
пытается найти ортогональные оси компонент с максимальной дисперсией в наборе
данных, тогда как задача LDA - найти подпространство признаков, которое оптими­
зирует разделимость классов. Оба метода, РСА и LDA, являются методами линей­
ного преобразования, которые могут использоваться для снижения числа размер­
ностей в наборе данных, где первый алгоритм - без учителя, а второй - с учителем.
Поэтому интуитивно можно подумать, что метод выделения признаков на основе
LDA лучше подходит для задач классификации, чем РСА.  Тем не менее, по сведени­
ям А. М. Мартинеса, в определенных случаях предобработка методом РСА, как пра­
вило, позволяет добиваться лучших результатов классификации при выполнении
задачи распознавания образов, например если каждый класс состоит из небольшого
числа образцов (А. М. Martinez, А. С. Kak. РСА Versus  LDA. Pattem Analysis and Ma-
chine Intelligence ( «РСА против LDA. Анализ образов и искусственный интеллект~.>).
IEEE Tгansactions on, 23(2):228-233, 2001).



Прежде чем в следующих подразделах мы рассмотрим внутреннее устройство
LDA, сначала резюмируем ключевые шаги алгоритма LDA:
1.  Стандартизировать d-мерный набор данных (d - это число признаков).
2.  Для каждого класса вычислить d-мерный вектор средних.
3.  Создать матрицу разброса между классами S8  и матрицу разброса внутри
классов Siv·
4.  Вычислить собственные векторы и соответствующие собственные значения
матрицы sv) s в .
5.  Выбрать k собственных векторов, которые соответствуют k самым большим
собственным значениям для построения dхk-матрицы преобразования  W;
собственные векторы являются столбцами этой матрицы.
6.  Спроецировать образцы на новое подпространство признаков при помощи
матрицы преобразования W.


"""

import matplotlib.pyplot as plt

"""
Анализ главных компонент (pгincipal component analysis,  РСА) - это метод ли­
нейного преобразования, относящийся к типу обучения без учителя, который ши­
роко используется в самых разных областях, чаще всего для снижения размерности.

"""

#==================================Общая и объясненная дисперсия ==============================
"""
Сначала начнем с загрузки набора данных сортов вин,
"""

#=================================Загрузка данных===============================================
import pandas as pd
import numpy as np

#===================================================================

from matplotlib.colors import ListedColormap
def plot_description_regions(X,y,classifier,test_idx=None,resolution=0.02):
    """реализуем небольшую вспомогательную функцию , которая визуально паказывает
    границы решений для двумерных наборов  данных"""

    #настроить генератор маркеров и палитру
    markers=('s','x','o','^','v')   #определяем маркера
    colors=('red','blue','lightgreen','gray','cyan')    #определяем цвета
    cmap=ListedColormap(colors[:len((np.unique(y)))])   #создаем палитрку

    #вывести поверхность решения
    x1_min,x1_max=X[:,0].min()-1,X[:,0].max()+1   #определяем мин и макс для 2 признаков
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1,xx2=np.meshgrid(np.arange(x1_min,x1_max,resolution),
                        np.arange(x2_min,x2_max,resolution))    #создаем пару матричных массивов на основе получившихся признаков
    Z=classifier.predict(np.array([xx1.ravel(),xx2.ravel()]).T)
    Z=Z.reshape(xx1.shape)
    plt.contourf(xx1,xx2,Z,alpha=0.4,cmap=cmap)
    plt.xlim(xx1.min(),xx1.max())
    plt.ylim(xx2.min(),xx2.max())

    #Показать Все образцы
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y==cl,0],y=X[y==cl,1],
                    alpha=0.8,c=cmap(idx),
                    marker=markers[idx],label=cl)
        #Выделить тестовые образцы
        if test_idx:
            X_test,Y_test=X[test_idx,:],y[test_idx]
            plt.scatter(X_test[:,0],X_test[:,1],c='',
                        alpha=1.0,linewidths=3,marker='o',
                        s=55,label='Тестовый набор')

#===================================================================


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data'

df_wine = pd.read_csv(url, header=None)  # считываем набор данных вин для проведения исследования

df_wine.columns = ['Метка класса', 'Алкоголь',
                       'Яблочная кислота', 'Зола',
                       'Щелочность золы', 'Магний',
                       'Всего фенола', 'Флаваноиды',
                       'Фенолы нефлаваноидные', 'Проантоцианины',
                       'Интенсивность цвета', 'Оттенок',
                       'OD280/OD315 разбавленныех вин', 'Пролин']
print('Метки классов:', np.unique(df_wine['Метка класса']))
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
X, y = df_wine.iloc[:, 1:].values, df_wine.iloc[:, 0].values
X_train, X_test, y_train, y_test = \
        train_test_split(X, y, test_size=0.3, random_state=0)

# ===================================Нормализация данных===============================
from  sklearn.preprocessing import MinMaxScaler

mms = MinMaxScaler()
X_train_norm = mms.fit_transform(X_train)
X_test_norm = mms.transform(X_test)
print(X_test_norm)
print('----------------------------------------------')
print(X_train_norm)
print('####################################################################################')
# ======================================Стандартизация===============================
from  sklearn.preprocessing import StandardScaler

stdsc = StandardScaler()
X_train_std = stdsc.fit_transform(X_train)
X_test_std = stdsc.transform(X_test)

print(X_test_std)
print('----------------------------------------------')
print(X_train_std)
print('####################################################################################')


#---------------------------------------------------------------
#-----------------------------Вычисление матриц разброса---------------

np.set_printoptions(precision=4)

mean_vecs=[]

for label in range(1,4):
    mean_vecs.append(np.mean(X_train_std[y_train==label],axis=0))
    print('BC %s: %s\n' %(label,mean_vecs[label-1]))

"""
Она вычисляется путем суммирования индивидуальных матриц разброса s; каж­
дого индивидуального класса i: 

"""
d=13 #число признаков
S_W=np.zeros((d,d))
for label,mv in zip(range(1,4),mean_vecs):
    class_scatter=np.zeros((d,d))
    for row in X_train[y_train==label]:
        row,mv=row.reshape(d,1),mv.reshape(d,1)
        class_scatter+=(row-mv).dot((row-mv).T)
        S_W+=class_scatter
print('Внутриклассовая матрица разброса : %sx%s' %(S_W.shape[0],S_W.shape[1]))

"""
Вследствие этого мы хотим прошкалировать индивидуальные матрицы разброса 
S;,  прежде чем просуммируем их как матрицу разброса S1v.  Во время разбивки мат­
рицы разброса на число образцов классов N; можно увидеть, что вычисление матри­
цы разброса фактически не отличается от вычисления ковариационной матрицы L;. 
Ковариационная матрица - это нормализованная версия матрицы разброса: 
"""


d  =  13  #  число признаков
S_W =  np .zeros((d,  d))
for  label, mv  in  zip(range(1,  4) ,  mean_vecs):
    class_scatter =  np.cov(X_train_std[y_train==label].T)
    S_W += class_scatter
print('Масштабированная внутриклассовая матрица разброса:  %sx%s'
% (S_W.shape[0] ,S_W .shape [1]))


"""
Вычислив масштабированную матрицу разброса внутри классов (или ковариаци­
онную матрицу), можно перейти к следующему шагу и вычислить матрицу разброса 
между классами S8: 

"""

mean_overall=np.mean(X_train_std,axis=0)
d=13  #число признаков
S_B=np.zeros((d,d))
for i,mean_vec in enumerate(mean_vecs):
    n=X_train[y_train==i+1,:].shape[0]
    mean_vec=mean_vec.reshape(d,1)
    mean_overall=mean_overall.reshape(d,1)
S_B+=n*(mean_vec-mean_overall).dot((mean_vec-mean_overall).T)
print('Межклассовая матрица разброса : %sx%s'%(S_B.shape[0],S_B.shape[1]))


#====================================Отбор линейных дискриминантов для нового подпространства признаков==================

"""
Оставшиеся шаги алгоритма LDA аналогичны шагам алгоритма РСА.  Однако вмес­
то выполнения разложения по собственным значениям на ковариационной матрице 
мы решаем обобщенную задачу на собственные значения матрицы
"""

eigen_vals,eigen_vecs=\
np.linalg.eig(np.linalg.inv((S_W).dot(S_B)))

"""
После того как мы вычислили собственные пары, теперь можно отсортировать 
собственные значения в убывающем порядке: 

"""

eigen_paits=[(np.abs(eigen_vals[i]),eigen_vecs[:,i])
             for i in range(len(eigen_vals))]
eigen_paits=sorted(eigen_paits,key=lambda k:k[0],reverse=True)

print('Собственные значения в убывающем порядке :\n')
for eigen_val in eigen_paits:
    print(eigen_val[0])


"""
Чтобы измерить, сколько информации о различении классов захвачено линейны­
ми дискриминантами (собственными векторами), построим график линейных дис­
криминантов по убыванию собственных значений, подобно графику объясненной 
дисперсии, который мы создали в разделе РСА. Для простоты назовем содержание 
информации о различении классов дискриминабельностью. 
"""

tot=sum(eigen_vals.real)
discr=[(i/tot) for i in sorted(eigen_vals.real,reverse=True)]
cum_discr=np.cumsum(discr)
plt.bar(range(1,14),discr,alpha=0.5,align='center',
        label='индивидуальная "дискриминабельность"')
plt.step(range(1,14),cum_discr,where='mid',
                                    label='кумулятивная "дискриминабельность"')
plt.ylabel('доля "дискриминабельности"')
plt.ylabel('Линейные дискриминанты')
plt.ylim([-0.1,1.1])
plt.legend(loc='best')
plt.show()

"""
Как видно на итоговом рисунке, первые два линейных дискриминанта захваты­
вают в тренировочном наборе данных сортов вин примерно 100% полезной инфор­
мации: 
"""


"""
Теперь объединим вертикально два наиболее отличительных столбца1  с собствен­
ными векторами, чтобы создать матрицу преобразования W: 

"""


w=np.hstack((eigen_paits[0][1][:,np.newaxis].real,
             eigen_paits[1][1][:,np.newaxis].real))
print('Матрица W:\n',w)

#============================Проекцирование образцов на новое простанство признаков=============

"""
При помощи матрицы преобразования W,  которую мы создали в предыдущем под­
разделе,  теперь можно преобразовать тренировочный набор данных путем умноже­
ния матриц: 

"""

X_train_lda=X_train_std.dot(w)
colors=['r','b','g']
markers=['s','x','o']
for l,c,m in zip(np.unique(y_train),colors,markers):
    plt.scatter(X_train_lda[y_train==l,0]*(-1),
               X_train_lda[y_train==l,1]*(-1),
                c=c,label=l,marker=m)

plt.xlabel('LD 1')
plt.ylabel('LD 2')

plt.legend(loc='lower right')
plt.show()

#=====================================Метод LDA в scikit-learn========================
"""
Пошаговая реализация была хорошим упражнением для понимания внутреннего 
устройства LDA  и понимания различий между алгоритмами LDA  и РСА. Теперь 
рассмотрим класс под названием LDA,  реализованный в библиотеке scikit-leaгn: 
"""

from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

lda=LinearDiscriminantAnalysis(n_components=2)
X_train_lda=lda.fit_transform(X_train_std,y_train)

"""
Затем посмотрим, как классификатор логистической регрессии обрабатывает бо­
лее низкоразмерный тренировочный набор данных после преобразования LDA: 

"""
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
lr=lr.fit(X_train_lda,y_train)
plot_description_regions(X_train_lda,y_train,classifier=lr)
plt.xlabel('LD 1')
plt.ylabel('LD 2')

plt.legend(loc='lower right')
plt.show()

"""
Понизив силу регуляризации, по-видимому, можно было бы сместить границы 
решения, в результате чего модели логистической регрессии будут правильно клас­
сифицировать все образцы в тренировочном наборе данных.  Впрочем, проанализи­
руем результаты на тестовом наборе: 

"""

X_test_lda=lda.transform(X_test_std)
plot_description_regions(X_test_lda,y_test,classifier=lr)
plt.xlabel('LD 1')
plt.ylabel('LD 2')

plt.legend(loc='lower right')
plt.show()