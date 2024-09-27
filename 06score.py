import pandas as pd
import time



path = './data/score.csv'
score = pd.read_csv(path, encoding='utf-8')
print(score)
print()

time.sleep(1)
# 문제 dept컬럼 103 출력

#선택지1 print(score[score.dept == 103])
#선택지2 print(score[score['dept']==103])
filtered_score = score[score['dept'] == 103]
print(filtered_score)
time.sleep(1)
# 문제2 kor컬럼 최대값 max()
max_kor = score['kor'].max()
print("kor 칼럼의 최대값:", max_kor)
time.sleep(1)
# 문제3 hap필드 = kor eng mat
# 문제4 avg필드 = hap/3
hap = score['kor']+score['eng']+score['mat']
avg = round(hap/3,2)
score.insert(5,['합계'],hap,True)
score.insert(6,['평균'],avg,True)
print(score)

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