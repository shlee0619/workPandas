import pandas as pd
import numpy as np
import time

path = './data/subway.csv'
df = pd.read_csv(path, encoding='utf-8', index_col=False)

print(df.shape)
print(df.describe())
print(df.info())
print(df)
print()

# 사용일자  노선명    역명  승차총승객수    하차총승객수  등록일자
# 문제1 노선명 한번 unique
print( df['노선명'].unique())
print()
print( df['노선명'].value_counts())
print()

# 문제2 승차총승객수 컬럼순으로 소트 역순차순
# print(df.sort_values(by='weight', ascending=False, ignore_index=True))

print(df.sort_values(by='승차총승객수', ascending=False, ignore_index=True))
print()


# 
# 문제3 loc[ 20:30 , 열 ], iloc[20:30-1  , 열 ]
print(df.head(15)) #무조건 0번째 시작
print()
print(df[0:15]) 
print()

# 문제4  2호선출력 조건출력 
print( df[ df['노선명']=='3호선' ])
print()


# 문제5  승차승객수 5만이상인  역명 
print( df[ df['승차총승객수'] > 50000]) 
print()
print( df[ df['승차총승객수'] > 50000]['역명'].unique()) 





# 사용일자  노선명    역명  승차총승객수    하차총승객수  등록일자
print()
print()