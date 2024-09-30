# matplotlib=차트 
import matplotlib.pyplot as plt
import matplotlib 
import time
import numpy as np
import pandas as pd


#from matplotlib  import font_manager,rc
font_name = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)

# 음수
import matplotlib as mpl 
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus'] = False

plt.rcParams['font.size']=12.0
plt.rcParams['font.family'] = 'batang'
plt.rcParams['font.family'] = 'Malgun Gothic'

fruits = ['apple', 'blue', 'kiwi', 'mango']
area =['서울','안양','수원','일산']
su1 = [21, 34, 45, 13]
su2 = [45, 19, 31, 50]
su3 = [33, 56, 27, 41]
su4 = [77, 26, 65, 29]


'''
지역별 과일 총판매수량
과일별 지역 총판매수량

조건1] 큰제목및 범례 x축제목 y축제목
조건2] bar모양권장 scatter, pie
조건3] y축값표시
조건4] df = pd.DataFrame({'서울':su1, '안양':su2,'수원'su3,'일산':su3}, index=fruits)
    이런 형태로 할것.

'''


df_region = pd.DataFrame({'서울': su1, '안양': su2, '수원': su3, '일산': su4}, index=fruits)

# 2. 과일별 지역 총판매수량 데이터프레임 생성 (전치행렬)
df_fruit = df_region.T  # 데이터프레임 전치 (행과 열을 바꿈)

# 막대 그래프 그리기 - 지역별 과일 총판매수량
fig, ax = plt.subplots(1, 2, figsize=(14, 6), layout='constrained')

# 1) 지역별 과일 총판매수량 그래프
x = np.arange(len(fruits))
width = 0.2  # 막대 너비
multiplier = 0

for column in df_region.columns:
    offset = width * multiplier
    rects = ax[0].bar(x + offset, df_region[column], width, label=column)
    ax[0].bar_label(rects, padding=3)
    multiplier += 1

ax[0].set_ylabel('판매수량')
ax[0].set_title('지역별 과일 총판매수량')
ax[0].set_xticks(x + width, fruits)
ax[0].legend(title="지역")

# 2) 과일별 지역 총판매수량 그래프
x = np.arange(len(area))
width = 0.2
multiplier = 0

for column in df_fruit.columns:
    offset = width * multiplier
    rects = ax[1].bar(x + offset, df_fruit[column], width, label=column)
    ax[1].bar_label(rects, padding=3)
    multiplier += 1

ax[1].set_ylabel('판매수량')
ax[1].set_title('과일별 지역 총판매수량')
ax[1].set_xticks(x + width, area)
ax[1].legend(title="과일")

plt.show()
