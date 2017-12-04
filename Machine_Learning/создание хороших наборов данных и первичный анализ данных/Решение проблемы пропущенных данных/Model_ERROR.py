import pandas as pd
from io import StringIO


csv_data='''A,B,C,D
            1.0,2.0,3.0,4.0
            5.0,6.0,8.0
            10.0,11.0,12.0'''


df=pd.read_csv(StringIO(csv_data))
print(df.values)


#======================Устранение образцов либо признаков спропущенными значениями=============
#  отбросить строки,  только если все столбцы содержат NaN
#df.dropna(how  ='all ' )


#  отбросить  строки,  если в  них менее  4  значений нe-NaN
#df.dropna(thresh=4 )


#отбросить строки,  если в  определенных столбцах  (здесь  ' С')  имеется NaN
#df.dropna(subset=[ 'C' ] )


#=============================Импутация пропущенных значений============

from sklearn.preprocessing import Imputer
imr=Imputer(missing_values='NaN',strategy='mean',axis=1)
imr=imr.fit(df)
imputd_data=imr.transform(df.values)
print(imputd_data)
