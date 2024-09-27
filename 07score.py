import pandas as pd
import time



path = './data/score.csv'
score = pd.read_csv(path, encoding='utf-8')
print(score)
print()


hap = score['kor']+score['eng']+score['mat']
avg = round(hap/3,2)
score.insert(5,['합계'],hap,True)
score.insert(6,['평균'],avg,True)
print(score)
print()
time.sleep(1)
# 문제5 index 3 ~ 10
# 행렬위치 loc[시작행:끝-1, 시작열:끝열]
print(score.loc[5:]) #5행부터 끝까지
time.sleep(1)
print(score.loc[3:10]) #3행부터 끝까지
time.sleep(1)

print('loc[s행:e행, 열]')
# 문제6 코드 = no컬럼, hap컬럼, avg컬럼
print(score[:,['no','합계','평균']]) #성공
#print(score.iloc[:, [0,5,6]) 이것도 성공






'''
    no  kor  eng  mat  dept
0   101   88   85   86   101
1   102   70   90   92   103
2   103   90   45   55   101
3   104   55   52   74   102
4   105   65   85   96   103
5   106   75   66   41   102
6   107   62   75   52   103
7   108   40   51   85   103
8   109   75   90   63   101
9   110   50   62   75   103
10  111   80   55   45   103
11  112   95   65   85   103
12  113   82   45   64   101
13  114   88   78   82   101
14  115   56   75   75   103
'''