import pandas as pd
import time




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