import pandas as pd
import time
#판다스 groupby 집합함수 sum() mean() max() mix()

path= './data/health.csv'
health = pd.read_csv(path)
print(health)
print()

#문제 height컬럼 weight컬럼 총점, 평균, 최대, 최소

hgroup = health.groupby(['HEIGHT'])['WEIGHT'].agg(['sum','mean','count'])

#설명: groupby(['항목'])은 항목을 기준으로 원소들을 나눈다
#agg는 새로운 칼럼이다.
#groupby(['항목']) 왼쪽에 ['또다른항목']을 넣으면 또다른 항목을 
# 기준에 따라 분류해보여준다.



print(hgroup)

print(health.groupby(['HEIGHT'])['WEIGHT'].describe())




# print(health.head(10))
# print()
# print(health.tail(10))

# print(health.info())
# print()
# print(health.describe())

   




print()

'''

df = pd.DataFrame(
     {
        'weight':  [68.9, 87.2, 45.0,  70.5, 47.0, 65.3], 
        'height':  [180, 190, 150,   160, 165, 170] ,
        'gender' : ['m', 'm', 'f',  'f', 'm', 'm']
    } 
)
print(df)
print()

#문제1 weight 소트
print(df.sort_values(by='weight', ascending=False))
print(df.sort_values(by='weight', ascending=True))
print()

#문제2 gender 소트
print(df.sort_values(by='gender'))
print()
print()

#문제3 height열데이터 추출
print(df.loc[:,'height':'gender']) #[시작행:끝행, 시작열:끝열]
print()


'''