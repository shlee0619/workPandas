import pandas as pd
import time



#데이터프레임직접 생성대신 파일처리 데이터가져오기
df = pd.DataFrame(
     {
        'weight':  [68.9, 87.2, 45.0,  70.5, 47.0, 65.3], 
        'height':  [180, 190, 150,   160, 165, 170] ,
        'gender' : ['m', 'm', 'f',  'f', 'm', 'm']
    } 
)


print(df)
print()
# 문제 height열데이터 추출
print('height gender 컬럼추출')
print(df.loc[:,'height':'gender']) #[시작행:끝행, 시작열:끝열]
print()

# 문제 weight >= 70 조건
print(df[df['weight']>=70].sort_values(by = 'height'))
print()

#문제 1행, 2행, 3행 [시:끝]
print(df[1:4])
print()



# 문제 2행부터 ~ 마지막까지
print(df[2:])


