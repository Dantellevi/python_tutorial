import matplotlib.pyplot as plt
import numpy as np

s = ['one','two','three ','four' ,'five']
x = [1, 2, 3, 4, 5]
z = np.random.random(100)
z1 = [10, 17, 24, 16, 22]
z2 = [12, 14, 21, 13, 17]

#Диаграмма()

fig=plt.figure()
plt.bar(x,z1)   #построение вертикальной диаграммы по данным
plt.title('Simple bar chart')
plt.grid(True)   # линии вспомогательной сетки


#Гистаграмма
fig = plt.figure()
plt.hist(z) #построение гистограммы
plt.title('Simple histogramm')
plt.grid(True)



#круговая диаграмма
fig=plt.figure()
plt.pie(x, labels=s)
plt.title('Simple pie chart')
plt.grid(True)




#специализированная диаграмма
# boxplot()
fig = plt.figure()
plt.boxplot([z1, z2])
plt.title('Simple box whisker chart')
plt.grid(True)

# errorbar()
fig = plt.figure()
plt.errorbar(x, z1, xerr=1, yerr=0.5)
plt.title('Simple error bar chart')
plt.grid(True)



plt.show()