# matplotlib=차트 
import matplotlib.pyplot as plt
import matplotlib 
import time
import numpy as np
import seaborn as sns

#from matplotlib  import font_manager,rc
font_name = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/malgun.ttf').get_name()
matplotlib.rc('font', family=font_name)

# 음수
import matplotlib as mpl 
mpl.rc('axes', unicode_minus=False)
mpl.rcParams['axes.unicode_minus'] = False

import pandas as pd
import time

path = './data/소상공인시장진흥공단_상가(상권)정보_서울_202112.csv'
df = pd.read_csv(path, encoding='utf-8')
print(df.head())
print()
print(df.info())

#상권업종대분류명
time.sleep(1)
cnt = df['상권업종대분류명'].value_counts()
print('', cnt)
'''
상권업종대분류명
음식          111654
소매           94320
생활서비스        58438
학문/교육        22765
부동산          14254
관광/여가/오락      7095
스포츠           4636
숙박            2132
'''

cntidx = df['상권업종대분류명'].value_counts().index
print('상권업종대분류명', cntidx)


#개수 복사
sosangX = df['상권업종대분류명'].value_counts().index
sosangY = df['상권업종대분류명'].value_counts()

# plt.figure(figsize=(12,6))
# sns.barplot(x=sosangX,y=sosangY)
# plt.show()

# plt.figure(figsize=(10,5))
# plt.bar(x=sosangX,height=sosangY,color='hotpink')
# plt.title('상권업종대분류명  데이터출력')
# plt.show()

plt.figure(figsize=(10,5))
# plt.scatter(sosangX,sosangY,marker='^')
plt.bar(sosangX,sosangY)
plt.title('상권업종대분류명  데이터출력')
plt.show()