from scipy.spatial.distance import pdist,squareform
from scipy import exp
from scipy.linalg import eigh
import numpy as np


def rbf_kernel_pca(X,gamma,n_components):
    """
    Реализация ядерного РСА с РБФ в качестве ядра

    :param X: форма=[n_samples,n_fuetuers]

    :param gamma: float- Настроечный параметр ядра РБФ
    :param n_components: imt -число возвращаемых главных компонентов
    :return:  X_pc{mumpy ndarray} , форама=[n_samples,k_features]
    Спроецированный набор данных
    """
    #Попарно вычислить квадратичные евклидовы расстояния
    #в наборе данных размера MxN
    sq_dists=pdist(X,'sqeuclidean')

    #попарно конвертировать расстояния в квадратную матрицу
    mat_sq_dists=squareform(sq_dists)

    #Вычислить симметричную матрицу ядра.
    K=exp(-gamma*mat_sq_dists)

    #Центрировать матрицу ядра
    N=K.shape[0]
    one_n=np.ones((N,N))/N
    K=K-one_n.dot(K)-K.dot(one_n)+one_n.dot(K).dot(one_n)


    #извлечь собственные пары из центированной матрицы ядра
    #Функция numpy.eigh возвращает их в отсортированном порядке
    eigvals,eigvecs=eigh(K)

    #Взять верхних к собственных векторов(спроецированные образцы)
    X_pc=np.column_stack(((eigvecs[:,-i]
                           for i in range(1,n_components+1))))
    return  X_pc

"""
Оборотная сторона использования ядерного РСА с РБФ в качестве ядра для сни­
жения размерности состоит в том, что нам нужно априорно определить параметр у. 
Для  нахождения надлежащего значения для у  требуется  поэкспериментировать, 
и это лучше всего делать при помощи алгоритмов настройки параметров, например 
поиска по сетке параметров, который мы более подробно обсудим в главе 6 ~изучение 
наиболее успешиых методов оценкu моделей и тонкой настройки гиперпараметров». 
"""


#=====================Пример 1. Разделение фигур в форме полумесяца ===============
"""
Теперь в качестве примера применим нашу функцию rЬf_kernel_pca к неким нели­
нейным наборам данных. Начнем с создания двумерного набора данных из 100  то­
чек образцов,  представляющих собой две фигуры в форме полумесяца: 

"""
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons
X,y=make_moons(n_samples=100,random_state=123)
plt.scatter(X[y==0,0],X[y==0,1],color='red',marker='^', alpha=0.5)
plt.scatter(X[y==1,0],X[y==1,1],color='blue',marker='o', alpha=0.5)
plt.show()
"""
В целях иллюстрации полумесяц,  состоящий из треугольных символов, будет 
представлять один класс, а полумесяц из круглых символов - образцы из другого 
класса: 
"""
#==============================


"""
Эти две фигуры полумесяца, безусловно, не являются линейно разделимыми, 
и наша задача состоит в том, чтобы развернуть полумесяцы ядерным методом РСА, 
в результате чего набор данных сможет подойти для передачи на вход линейно­
го классификатора.  Но сначала посмотрим, как выглядит набор данных, если его 
спроецировать на главные компоненты стандартным методом РСА: 

"""

from sklearn.decomposition import PCA
scikit_pca=PCA(n_components=2)
X_spca=scikit_pca.fit_transform(X)
fig,ax=plt.subplots(nrows=1,ncols=2,figsize=(7,3))
ax[0].scatter(X_spca[y==0,0],X_spca[y==0,1],
              color='red',marker='^',alpha=0.5)
ax[0].scatter(X_spca[y==1,0],X_spca[y==1,1],
              color='blue',marker='o',alpha=0.5)


ax[1].scatter(X_spca[y==0,0],np.zeros((50,1))+0.02,
              color='red',marker='^',alpha=0.5)
ax[1].scatter(X_spca[y==1,0],np.zeros((50,1))-0.02,
              color='blue',marker='o',alpha=0.5)


ax[0].set_xlabel('PC1')
ax[0].set_ylabel('PC2')
ax[1].set_ylim([-1,1])
ax[1].set_yticks([])
ax[1].set_xlabel('PC1')
plt.show()
"""
На итоговом рисунке четко видно, 
что линейный классификатор не сможет хоро­
шо сработать на наборе данных, 
преобразованном стандартным методом РСА: 
"""


"""
Теперь испытаем нашу функцию ядерного РСА rЬf_kernel_pca, 
которую мы реали­
зовали в предыдущем подразделе: 

"""
from matplotlib.ticker import  FormatStrFormatter
X_kpca=rbf_kernel_pca(X,gamma=15,n_components=2)
fig,ax=plt.subplots(nrows=1,ncols=2,figsize=(7,3))

ax[0].scatter(X_kpca[y==0,0],X_kpca[y==0,1],
              color='red', marker='^', alpha=0.5)
ax[0].scatter(X_kpca[y==1,0],X_kpca[y==1,1],
              color='blue', marker='o', alpha=0.5)

ax[1].scatter(X_kpca[y==0,0],np.zeros((50,1))+0.02,
              color='red',marker='^',alpha=0.5)
ax[1].scatter(X_kpca[y==1,0],np.zeros((50,1))-0.02,
              color='blue',marker='o',alpha=0.5)


ax[0].set_xlabel('PC1')
ax[0].set_ylabel('PC2')
ax[1].set_ylim([-1,1])
ax[1].set_yticks([])
ax[1].set_xlabel('PC1')

ax[0].xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
ax[1].xaxis.set_major_formatter(FormatStrFormatter('%0.1f'))
plt.show()

"""
Теперь видно, что эти два класса (круги и треугольники) хорошо линейно разде­
лены, и поэтому преобразованные данные стали тренировочным набором, который 
подходит для передачи на вход линейных классификаторов: 

"""


#===========================Пример 2- Разделение концентрических кругов========================
