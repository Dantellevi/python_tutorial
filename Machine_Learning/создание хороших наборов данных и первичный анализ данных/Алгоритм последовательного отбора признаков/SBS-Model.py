"""

В основе алгоритма SBS  лежит довольно простая идея: SBS  последовательно
удаляет признаки из полнопризнакового подмножества, пока новое подпростран­
ство признаков не будет содержать нужное число признаков. Для определения того,
какой признак удалять на каждом шаге, нам нужно определить критериальную
функцию], которую мы хотим минимизировать. Вычисленный данной функцией
критерий может быть просто разницей в качестве классификатора после и до уда­
ления отдельно взятого признака. Тогда удаляемый на каждом шаге признак можно
просто определить как признак, который максимизирует этот критерий; или в более
интуитивных терминах на каждом шаге мы устраняем признак, который вызывает
наименьшую потерю качества после удаления. Основываясь на предыдущем опре­
делении алгоритма SBS, его можно в общих чертах обрисовать в 4 простых шагах:
1.  Инициализировать алгоритм, назначив k =  d,  где d - это размерность полно­
признакового пространства.
2.
3.
4.
с+
Определить признак х, который максимизирует критерий х =  aгgmax](Xk - х),
Где ХЕ Xk.
Удалить признак х из набора признаков: Хн := Xk  - х; k := k - 1.
Закончить, если k равняется числу требуемых признаков, в противном случае
перейти к шагу 2.
"""


from sklearn.base import clone
from itertools import combinations
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


class SBS():
    """
    В приведенной выше реализации мы установили параметр k_features в требуемое
число признаков, которые мы хотим получить. По умолчанию мы используем метрику
accuracy_score из библиотеки scikit-learn, которая оценивает качество модели, и оцен­
щик для классификации на подмножествах признаков. Внутри цикла while в методе
fit созданные функцией itertools.comblnatlon  подмножества признаков оцениваются
и сужаются, пока подмножество признаков не получит требуемую размерность. На
каждой итерации оценка верности (accuracy_score)  наилучшего подмножества нака­
пливается в списке self.scoгes_,  основываясь на создаваемом внутри тестовом наборе
данных X_test. Мы воспользуемся этими показателями позже для оценки результатов.
Индексы столбцов окончательного подмножества признаков назначаются списку self.
indices_,  который используется методом tгansform для возврата нового массива дан­
ных со столбцами отобранных признаков. Отметим, что, вместо того чтобы вычислять
критерий явным образом внутри метода fit, мы просто удалили признак, который не
содержится в подмножестве наиболее перспективных признаков.

    """
    def __init__(self,estimator,k_features,scoring=accuracy_score,test_size=0.25,random_state=1):
        self.scoring=scoring
        self.estimator=clone(estimator)
        self.k_features=k_features
        self.test_size=test_size
        self.random_state=random_state


    #Метод обучения модели
    def fit(self,X,y):
        X_train,X_test,y_train,y_test=\
        train_test_split(X,y,test_size=self.test_size,random_state=self.random_state)
        dim=X_train.shape[1]
        self.indices=tuple(range(dim))
        self.subsets=[self.indices]
        score=self.calc_score(X_train,y_train,X_test,y_test,self.indices)
        self.scores_=[score]
        while dim>self.k_features:
            scores=[]
            subsets=[]
            for p in combinations(self.indices,r=dim-1):
                score=self.calc_score(X_train,y_train,X_test,y_test,p)
                scores.append(score)
                subsets.append(p)
            best=np.argmax(scores)
            self.indices=subsets[best]
            self.subsets.append(self.indices)
            dim-=1

            self.scores_.append(scores[best])

        self.k_score_=self.scores_[-1]

        return self

    def transform(self,X):
        return X[:,self.indices]


    def calc_score(self,X_train,y_train,X_test,y_test,indices):
        self.estimator.fit(X_train[:,indices],y_train)
        y_pred=self.estimator.predict(X_test[:,indices])
        score=self.scoring(y_test,y_pred)
        return score



if __name__=='__main__':
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
    #========================================================================
    """
    Теперь посмотрим на нашу реализацию SBS в действии, воспользовавшись для 
этого классификатором KNN из библиотеки scikit-learп: 
    """

    from sklearn.neighbors import KNeighborsClassifier
    import matplotlib.pyplot as plt
    knn=KNeighborsClassifier(n_neighbors=2)
    sbs=SBS(knn,k_features=1)
    sbs.fit(X_train_std,y_train)
    """
     построим график верности классификации классификатора KNN,  ко­
торый был вычислен на перекрестно-проверочном наборе данных.
    """
    k_feat=[len(k) for k in sbs.subsets]
    plt.plot(k_feat,sbs.scores_,marker='o')
    plt.ylim([0.7,1.1])
    plt.ylabel('Верность')
    plt.xlabel('Число признаков')

    """
    Ради удовлетворения собственного любопытства посмотрим, какие это пять 
признаков, которые привели к такому хорошему качеству на проверочном наборе 
данных: 
    """

    k5=list(sbs.subsets[8])
    print(df_wine.columns[1:][k5])

    """
    Теперь выполним оценку качества классификатора KNN на исходном тестовом 
наборе: 
    """
    knn.fit(X_train_std, y_train)
    print('Верность на тренировочном наборе:',knn.score(X_train_std,y_train))
    print('Верность на тестовом наборе:',knn.score(X_test_std,y_test))

    """
    Теперь воспользуемся отобранным 5-признаковым подмножеством и по­
смотрим на качество KNN: 
    """

    knn.fit(X_train_std[:,k5],y_train)
    print('Верность на тренировочном наборе:', knn.score(X_train_std[:,k5], y_train))
    print('Верность на тестовом наборе:', knn.score(X_test_std[:,k5], y_test))
    plt.grid()
    plt.show()


