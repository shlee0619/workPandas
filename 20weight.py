import pandas as pd
import time


df=pd.DataFrame({
    'weight':  [68.9, 87.2, 45.0,  70.5, 47.0, 65.3], 
    'height':  [180, 190, 150,   160, 165, 170] ,
    'gender' : ['m', 'm', 'f',  'f', 'm', 'm']
    })

print(df)
df_group = df.groupby('gender')
#print(df_group) <pandas.core.groupby.generic.DataFrameGroupBy object at 0x0000021CE8B00B00>
time.sleep(1)
print()
for key,value in df_group:
    print(key, '', value)
    print()

'''
f     weight  height gender
2    45.0     150      f
3    70.5     160      f

m     weight  height gender
0    68.9     180      m
1    87.2     190      m
4    47.0     165      m
5    65.3     170      m
'''







print()







