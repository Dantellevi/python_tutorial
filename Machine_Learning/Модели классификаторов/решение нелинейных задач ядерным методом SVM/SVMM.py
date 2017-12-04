import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from sklearn import datasets
from sklearn.svm import SVC
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


#---------------------------------------------------------------------------
iris=datasets.load_iris()   #подгружаем данные

X=iris.data[:,[2,3]]    #матрица признаков -длинна и ширина
y=iris.target
print(np.unique(y))     #возращает название образцов в виде массива (0,1,2)

#================<разделение данных на тренеровочные и тестовые>===============
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=0)    #тестовые данные 30% тренеровочные 70%
#================================================


#=======================<Стандартизация признаков>===========

from sklearn.preprocessing import StandardScaler
sc=StandardScaler()     #класс стандартизатор признаков
sc.fit(X_train)         #вычисляем среднее и отклонение  для каждой размерности признаков из тренеровочных данных

X_train_std=sc.transform(X_train)   #стандартизируем данные
X_test_std=sc.transform(X_test)

X_com_std=np.vstack((X_train_std,X_test_std))
y_com=np.hstack((y_train,y_test))




#==================================================
svm=SVC(kernel='rbf',random_state=0,gamma=100.0,C=1.0)  #используем нелинейное ядро rbf(ядром из функции радиального базиса)(параметр gamma-параметр отсечения для гауссовой сферы)
svm.fit(X_train_std,y_train)
plot_description_regions(X_com_std,y_com,classifier=svm,test_idx=range(105,150))
plt.xlabel('Длина лепестка[стандартизированная]')
plt.ylabel('ширина лепестка [стандартизированная]')
plt.legend(loc='upper left')
plt.show()
#=============================================================================
X_xor=np.random.randn(200,2)
y_xor=np.logical_xor(X_xor[:,0]>0,X_xor[:,1]>0)
y_xor=np.where(y_xor,1,-1)
# plt.scatter(X_xor[y_xor==1,0], X_xor[y_xor==1,1],c='b',marker='x',label='1')
# plt.scatter(X_xor[y_xor==-1,0], X_xor[y_xor==-1,1],c='r',marker='s',label='-1')
# plt.ylim(-3.0)
# plt.legend()

svm=SVC(kernel='rbf',random_state=0,gamma=0.10,C=10.0)  #используем нелинейное ядро rbf(ядром из функции радиального базиса)(параметр gamma-параметр отсечения для гауссовой сферы)
svm.fit(X_xor,y_xor)
plot_description_regions(X_xor,y_xor,classifier=svm)
plt.legend(loc='upper left')
plt.show()

