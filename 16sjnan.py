import pandas as pd
import numpy as np
import time

#결측값 파일대신 Key:Value 딕트구조를 프레임화 = table화 
data = {
    'code':range(2000,2010),
    'kor': [85, 95, 75, 70, 100, np.nan, 95, 85, 80, 85],
    'eng': [95,  np.nan, 100, 85, 80, 85, 95, 95, np.nan, 70],
    'mat': [np.nan, np.nan, np.nan, 0, 0, 0, 0, 95, np.nan, 70],   }
df = pd.DataFrame(data)
print(df)
print()
print()

# print( df.isna()) #널이면 True,  데이터가 있으면 False
# print('널정보', df.isnull().sum()) 
# 비권장 print('널정보', df.isna().size) 
print('널정보', df.isna().sum()) 
print()
print('널정보', df.isnull().sum())  



# print('df.dropna()테스트중')
# df=df.dropna()
# print(df)
# # print()
# # time.sleep(1)

# print('df.fillna(0)테스트중')
# df=df.fillna(0) #결측값 대체 nan값을 0으로 대체 
# print(df)
# print()




hap = df['kor']+df['eng']+df['mat']
df.insert(4, ['hap'], hap, True )
# print(df)
print()
print()
