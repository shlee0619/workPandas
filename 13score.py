import pandas as pd

score = pd.read_csv('./data/score.csv', encoding = 'cp949')
hap = score['kor']+score['eng']+score['mat']
avg = round(hap/3,2)
score.insert(5,['hap'],hap,True)
score.insert(6,['avg'],avg,True)
print(score)
print()
print('-'*50)

print()
print('무작위')
score_sample = score.sample(7)
print(score_sample)
print()
print()