import pandas as ps
import numpy as np
"""
Будем показывать основные методы в деле, 
анализируя набор данных по оттоку клиентов 
телеком-оператора
"""

#=================================================================================
df=ps.read_csv('telecom_churn.csv') #читаем данные из файла
#=================================================================================
print('----------------------Получаем первые признаки(столбцы) из данных-----------------------')

print(df.head())       #посмотрим на первые 5 строк
print('----------------------------------------------------------------------------------------------')
#=================================================================================
"""
Каждая строка представляет собой одного клиента – это объект исследования.
Столбцы – признаки объекта.

Название	Описание	Тип
State	Буквенный код штата	номинальный
Account length	Как долго клиент обслуживается компанией	количественный
Area code	Префикс номера телефона	количественный
International plan	Международный роуминг (подключен/не подключен)	бинарный
Voice mail plan	Голосовая почта (подключена/не подключена)	бинарный
Number vmail messages	Количество голосовых сообщений	количественный
Total day minutes	Общая длительность разговоров днем	количественный
Total day calls	Общее количество звонков днем	количественный
Total day charge	Общая сумма оплаты за услуги днем	количественный
Total eve minutes	Общая длительность разговоров вечером	количественный
Total eve calls	Общее количество звонков вечером	количественный
Total eve charge	Общая сумма оплаты за услуги вечером	количественный
Total night minutes	Общая длительность разговоров ночью	количественный
Total night calls	Общее количество звонков ночью	количественный
Total night charge	Общая сумма оплаты за услуги ночью	количественный
Total intl minutes	Общая длительность международных разговоров	количественный
Total intl calls	Общее количество международных разговоров	количественный
Total intl charge	Общая сумма оплаты за международные разговоры	количественный
Customer service calls	Число обращений в сервисный центр	количественный




Целевая переменная: Churn – Признак оттока, бинарный признак (1 – потеря клиента, то есть отток).
 Потом мы будем строить модели, прогнозирующие этот признак по остальным, поэтому мы и назвали его целевым.
"""
#=================================================================================================================
print('----------------------Получаем размер и общую информацию о данных-----------------------')
print(df.shape)         #размер данных, названия признаков и их типы

print(df.info())                #Общая информация по датафрейму

print('--------------------------------------------------------------------------------------------')

#====================================================================================================================
"""
Изменить тип колонки можно с помощью метода astype. Применим этот метод к признаку Churn и переведём его в int64:
"""
print('--------------------------------Изменяет тип данных в колонке Churn--------------------------------')
df['Churn'] = df['Churn'].astype('int64')       #переводим занчения из столбца churn  в целочисленное значение

print('-----------------------------------------------------------------------------------------------------')
#-----------------------------------------------------------------------------------------------------------------------
"""
Метод describe показывает основные статистические характеристики
 данных по каждому числовому признаку (типы int64 и float64): 
 число непропущенных значений, среднее, стандартное 
 отклонение, диапазон, медиану, 0.25 и 0.75 квартили.
"""
print('-----------------------------показывает основные статистические характеристики данных по каждому числовому признаку----------------')

print(df.describe())

print('---------------------------------------------------------------------------------------------------------')
#-----------------------------------------------------------------------------------------------------------------------
"""
Чтобы посмотреть статистику по нечисловым признакам, нужно явно указать интересующие нас типы в параметре include.
"""

print('-----------------------------------------Информацию по нечисловым признакам данных---------------------------')
print(df.describe(include=['object', 'bool']))

print('-----------------------------------------------------------------------------------------------------------------')
#--------------------------------------------------------------------------------------------------------------------------
"""
Для категориальных (тип object) и булевых (тип bool) признаков можно 
воспользоваться методом value_counts. 
Посмотрим на распределение данных по нашей целевой переменной — Churn:
"""
print('-------------------------Распределение данных в целевой колонке-Churn-отток клиентов')
print(df['Churn'].value_counts())

print('------------------------------------------------------------------------------------------------------------')
#------------------------------------------------------------------------------------------------------------------------
"""
Посмотрим на распределение пользователей по переменной Area code. 
Укажем значение параметра normalize=True, чтобы посмотреть не абсолютные частоты, а относительные.
"""
print('----------------------------------Распределение пользователей индексы номеров телефона----------------')
print(df['Area code'].value_counts(normalize=True))
print('-------------------------------------------------------------------------------------------------------')

#=========================================================Сортировка==========================================================================
"""
DataFrame можно отсортировать по значению какого-нибудь из признаков. 
В нашем случае, например, по Total day charge 
(ascending=False для сортировки по убыванию):
"""
print('----------------------------------Сортируем данные по Общай сумме оплаты за услуги днем------------------------')
print(df.sort_values(by='Total day charge',
        ascending=False).head())
print('-------------------------------------------------------------------------------------------------------')

#-----------------------------------------------------------------------------------------------------------------------
#===================================Сортировать можно и по группе столбцов:
print('----------------------------------Сортируем данные по группе столпцов отток , и общее количество дней------------------------')
print(df.sort_values(by=['Churn', 'Total day charge'],
        ascending=[True, False]).head())
print('-------------------------------------------------------------------------------------------------------')
#-----------------------------------------------------------------------------------------------------------------------

#===============================================Индексация и извлечение данных===================================================================
"""
DataFrame можно индексировать по-разному. В связи с этим рассмотрим 
различные способы индексации и извлечения нужных нам данных из 
датафрейма на примере простых вопросов.


Для извлечения отдельного столбца можно использовать конструкцию вида 
DataFrame['Name']. Воспользуемся этим для ответа 
на вопрос: какова доля людей нелояльных пользователей в нашем датафрейме?
"""
print('---процент не лояльных пользователей---')
print(df['Churn'].mean())               #процент не лояльных пользователей

"""
14,5% — довольно плохой показатель для компании, с 
таким процентом оттока можно и разориться.


Очень удобной является логическая индексация DataFrame по одному столбцу. 
Выглядит она следующим образом: df[P(df['Name'])], где P — это некоторое логическое условие, 
проверяемое для каждого элемента столбца Name. Итогом такой индексации является DataFrame, состоящий только из строк, 
удовлетворяющих условию P по столбцу Name.


Воспользуемся этим для ответа на вопрос: каковы средние значения числовых признаков среди нелояльных пользователей?
"""
print('---среднее значение числовых признаков среди нелояльных пользователей---')
print(df[df['Churn']==1].mean())       #среднее значение числовых признаков среди нелояльных пользователей

"""
Скомбинировав предыдущие два вида индексации, 
ответим на вопрос: сколько в среднем в течение 
дня разговаривают по телефону нелояльные 
пользователи?
"""
print('---сколько в среденем разгаваривают по телефону нелояльные пользователи---')
print(df[df['Churn']==1]['Total day minutes'].mean())   #сколько в среденем разгаваривают по телефону нелояльные пользователи



"""
Какова максимальная длина международных звонков среди 
лояльных пользователей (Churn == 0), не пользующихся 
услугой международного 
роуминга ('International plan' == 'No')?
"""
print('---максимальная длина международных звонков среди лояльных пользователей не пользующихся услугой международного роуминга---')
print(df[df['Churn']==0&(df['International plan']=='No')]['Total intl minutes'].max())  #максимальная длина международных звонков среди лояльных пользователей не пользующихся услугой международного роуминга

print('---вывод определенных данных(первые пять строк с полями от state до Area code)---')
print(df.loc[0:5,'State':'Area code']) #вывод определенных данных(первые пять строк с полями от state до Area code)
#либо так
print('---вывод определенных данных(первые пять строк с полями от state до Area code)---')
print(df.iloc[0:5, 0:3])

"""
Если нам нужна первая или последняя строчка датафрейма, 
пользуемся конструкцией 
df[:1] или df[-1:]:
"""
print('-------------------------------Последняя строка датафрейма----------------')
print(df[-1:])


#======================================Применение функций к ячейкам, столбцам и строкам==========================



#Применение функции к каждому столбцу: apply

print('-------------------------------Поиск максимальных значений в каждом столбце----------------')
print(df.apply(np.max))

#------------------------------------------------------

#====================================Применение функции к каждой ячейке столбца=============
"""
Например, метод map можно использовать для замены значений в 
колонке, передав ему в качестве аргумента словарь 
вида {old_value: new_value}:
"""

d={'No':False,'Yes':True}
print('-------------------------------замена значений----------------')
df['International plan']=df['International plan'].map(d)
print(df.head())

print('-------------------------------замена значений----------------')
#Аналогичную операцию можно провернуть с помощью метода replace:

df = df.replace({'Voice mail plan': d})
print(df.head())
#----------------------------------------------------------

#===============================Группировка данных=====================

#В общем случае группировка данных в Pandas выглядит следующим образом:
columns_to_show = ['Total day minutes', 'Total eve minutes', 'Total night minutes']

#Группирование данных в зависимости от значения признака Churn и вывод статистик по трём столбцам в каждой группе.
df.groupby(['Churn'])[columns_to_show].describe(percentiles=[])
#--------------------------------------------------------------------------------------------------------------------

#Сделаем то же самое, но немного по-другому, передав в agg список функций:
df.groupby(['Churn'])[columns_to_show].agg([np.mean, np.std, np.min, np.max])
#-------------------------------------------------------------------------------------





#================================Сводные таблицы===========================


"""
Допустим, мы хотим посмотреть, как наблюдения в нашей выборке 
распределены в контексте двух признаков — Churn и 
International plan. Для этого мы можем построить таблицу 
сопряженности, воспользовавшись методом crosstab:
"""
print('-------------------------------Сводные таблицы-----------------')
print(ps.crosstab(df['Churn'], df['International plan']))
#---------------------------------------------------------------------------
#Давайте посмотрим среднее число дневных, вечерних и ночных звонков для разных Area code:

print(df.pivot_table(['Total day calls', 'Total eve calls', 'Total night calls'],
['Area code'], aggfunc='mean').head(10))
#----------------------------------------------------------------------------

#===========================================Преобразование датафреймов======================

"""
Например, мы хотим посчитать общее количество звонков для всех пользователей
. Создадим объект total_calls типа Series и 
вставим его в датафрейм:
"""
print('-------------------------------Преобразование датафреймов(посчитать общее количество звонков для всех пользователей(вставим его в датафрейм))---------------------------------')
total_calls = df['Total day calls'] + df['Total eve calls'] + \
                  df['Total night calls'] + df['Total intl calls']
df.insert(loc=len(df.columns), column='Total calls', value=total_calls)
# loc - номер столбца, после которого нужно вставить данный Series
# мы указали len(df.columns), чтобы вставить его в самом конце
print(df.head())


"""
Добавить столбец из имеющихся можно и проще, не создавая промежуточных Series:
"""
df['Total charge'] = df['Total day charge'] + df['Total eve charge'] + df['Total night charge'] + df['Total intl charge']
print('-------------------------------Добавить столбец из имеющихся можно и проще, не создавая промежуточных Series---------------------------------')
print(df.head())

"""
Чтобы удалить столбцы или строки, воспользуйтесь методом drop, передавая в качестве аргумента нужные индексы и требуемое значение параметра axis 
(1, если удаляете столбцы, и ничего или 0, если удаляете строки):
"""
print('-------------------------------избавляемся от созданных только что столбцов и строк---------------------------------')
# избавляемся от созданных только что столбцов
df = df.drop(['Total charge', 'Total calls'], axis=1)

df.drop([1, 2]).head() # а вот так можно удалить строчки

print(df.head())



print('=============================================Первые попытки прогнозирования оттока===================================================')


"""
Посмотрим, как отток связан с признаком "Подключение международного роуминга" (International plan). 
Сделаем это с помощью сводной таблички crosstab, а также путем иллюстрации с Seaborn 
(как именно строить такие картинки и анализировать с их помощью графики – материал следующей статьи).
"""
print('Посмотрим, как отток связан с признаком "Подключение международного роуминга (International plan)')
print('Сделаем это с помощью сводной таблички crosstab, а также путем иллюстрации с Seaborn')
print('(как именно строить такие картинки и анализировать с их помощью графики – материал следующей статьи).')
print(ps.crosstab(df['Churn'], df['International plan'], margins=True))
print("""
Видим, что когда роуминг подключен, доля оттока намного выше – интересное наблюдение! Возможно, большие и плохо контролируемые траты в роуминге очень конфликтогенны и приводят к недовольству клиентов телеком-оператора и, соответственно, к их оттоку.
""")
print('---------------------------------------------------------------------------')
print("""
Видим, что когда роуминг подключен, доля оттока намного выше – интересное наблюдение! Возможно, большие и плохо контролируемые траты в роуминге очень конфликтогенны и приводят к недовольству клиентов телеком-оператора и, соответственно, к их оттоку.


Далее посмотрим на еще один важный признак – "Число обращений в сервисный центр" (Customer service calls). Также построим сводную таблицу и картинку.
""")
print(ps.crosstab(df['Churn'], df['Customer service calls'], margins=True))
print("""
Может быть, по сводной табличке это не так хорошо видно (или скучно ползать взглядом по строчкам с цифрами), а вот картинка красноречиво свидетельствует о том, что доля оттока сильно возрастает начиная с 4 звонков в сервисный центр.


Добавим теперь в наш DataFrame бинарный признак — результат сравнения Customer service calls > 3. И еще раз посмотрим, как он связан с оттоком.
""")

df['Many_service_calls'] = (df['Customer service calls'] > 3).astype('int')
ps.crosstab(df['Many_service_calls'], df['Churn'], margins=True)
print("""
Объединим рассмотренные выше условия и построим сводную табличку для этого объединения и оттока.
""")
ps.crosstab(df['Many_service_calls'] & df['International plan'] , df['Churn'])
