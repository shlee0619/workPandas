import pandas as pd
import numpy as np
print()


#결측값 파일대신 Key:Value 딕트구조를 프레임화 = table화
data = {'code':range(2000,2010),
        'kor':[85,95,np.nan,70,100,np.nan,95,np.nan,80,85],
        'eng':[95,70,100,85,80,85,95,95,np.nan,70],
        'mat':[np.nan, np.nan, np.nan, 0,0,0,0, 95, np.nan, 75]

}
df = pd.DataFrame(data)
print(df)
print()
print()

print(df.head())#기본5개
print()
print(df.tail())#기본5개

df = df.fillna(0)
print(df)
print()

print(df.info())

print()
print(df.shape)

print()
print(df.describe())

print(df['eng'].unique())

#문제 kor점수 소트 역순으로
print(df.sort_values(by='kor' ,ascending= False, ignore_index=True))

