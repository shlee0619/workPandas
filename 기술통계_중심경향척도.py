import pandas as pd

import numpy as np
df = pd.DataFrame({'name': ["Richard", "Sara", "Andrea", "Steven", "Jordan", "Pam",
                            "Michael", "Liz", "Nicole", "Mike", "Kent", "Elizabeth",
                            "Bill", "Hadley", "Buffy", "Chip", "Homer", "Margaret",
                            "Courtney", "Leonard", "Jeffrey", "Emily"],
                   'major': ["교육학", "심리학", "교육학", "심리학", "교육학", "교육학",
                             "심리학", "심리학", "화학", "간호학", "역사학", "영어영문학",
                             "심리학", "심리학", "교육학", "교육학", "심리학", "영어영문학",
                             "심리학", "심리학", "화학", "스페인어"],
                   'age': [19, 18, 19, 21, 20, 24, 21, 19, 19, 20, 18, 21, 22, 23, 21, 19,
                           18, 22, 24, 21, 18, 19]})

df['major'].value_counts()
df['age'].mean()
customers = [2150, 1534, 3564]
np.mean(customers)
sum(customers)
len(customers)
sum(customers)/len(customers)
# 편차
x = [3,4,5]
x_bar = np.mean(x);x_bar
x_dev = x - x_bar;x_dev
sum(x_dev)
# 가중평균
score = pd.Series([97, 94, 92, 91, 90, 89, 78, 60])
freq = pd.Series([4, 11, 12, 21, 30, 12, 9, 1])
# 점수*빈도
score_freq = score*freq
score_freq
# 분자
sum(score_freq)