import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import matplotlib 

train = pd.read_csv('./data/train.csv')


title_mapping={
    'Mr':0, 'Miss':1, 'Mrs':2,
    'Master':3, 'Dr':3, 'Rev':3, 'Col':3, 'Major':3, 'Mlle':3, 'Countess':3,
    'Ms':3, 'Lady':3, 'Jonkheer':3, 'Don':3, 'Dona':3, 'Mme':3, 'Capt':3, 'Sir':3
}
#문제1 결측값 nan값 sum
print("\n결측값 nan값 sum")
print(train.isnull().sum())
#문제2 Sex성별의 인원수, Pclass 필드의 인원수
print("Sex성별의 인원수")
print(train['Sex'].value_counts())
print("\nPclass 필드의 인원수")
print(train['Pclass'].value_counts())
#문제3 Pclass필드 == 1
print("\nQ3: Pclass필드 == 1")
print(train[train['Pclass'] == 1])
#문제4 Sex성별=='female' 출력
print("\n Q4: Sex성별=='female' 출력")
print(train[train['Sex']=='female'])
#문제5 Age필드의 naa널값을 나이의 평균값으로 채우기
print("\nQ5: Age필드의 naa널값을 나이의 평균값으로 채우기")
mean_age = train['Age'].mean()
train['Age'].fillna(mean_age, inplace=True)

print(train['Age'])


# 호칭데이터를 좀더 빠르게 머신학습처리를 위해서 숫자화 0Mr 1Miss 2Mrs 3기타
# Title 컬럼생성후 이름컬럼뒤에 추가 train.insert(위치, 가짜컬럼)
# 숫자로 분류시키기 (Title map) => Title 컬럼
# Mr: 0
# Miss: 1
# Mrs: 2
# Others: 3
train['Title'] = train['Name'].str.extract(' ([A-Za-z]+)\.', expand=False)
train['Title'] = train['Title'].map(title_mapping)
train['Title'].fillna(3, inplace=True)
name_index = train.columns.get_loc('Name')
train.insert(name_index + 1, 'Title', train.pop('Title'))
print(train.head())





